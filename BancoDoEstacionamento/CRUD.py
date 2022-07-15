import mysql.connector
from datetime import datetime


class Crudestacionamento:
    def __init__(self, placa=None, nome=None, modelo=None, cor=None, concessionaria=None, vaga=None,
                 qtd_selecionada=None):
        self.placa = placa
        self.nome = nome
        self.modelo = modelo
        self.cor = cor
        self.concessionaria = concessionaria
        self.vaga = vaga
        self.quantidade_selecionada = qtd_selecionada
        self.cliente = None
        self.results = None
        self.quantidade_clientes = None
        self.vagas = None
        self.list_clientes = None
        self.verifica = False
        self.nrm_vaga = None
        self.chegada = None
        self.saida = None
        self.nrm_das_vagas = []
        self.con = mysql.connector.connect(host='localhost', user='root', password='', database='estacionamento')

        if self.con.is_connected():
            pass

    def read_registros(self):
        cursor = self.con.cursor()
        sql = f'SELECT * FROM registros_gerais WHERE Placa = "{self.placa}"'
        cursor.execute(sql)
        results = cursor.fetchall()
        # cursor.close()
        # self.con.close()

        self.quantidade_clientes = 0
        for placa, nome, modelo, cor, concessionaria, identificador in results:
            self.quantidade_clientes += 1
            self.nome = nome
            self.modelo = modelo
            self.cor = cor
            self.concessionaria = concessionaria
        vaga = f'SELECT * FROM registros_de_vagas WHERE Placa = "{self.placa}"'
        cursor.execute(vaga)

        results_vaga = cursor.fetchall()

        for _, nrm_vaga, chegada, saida in results_vaga:
            self.nrm_vaga = nrm_vaga
            self.chegada = chegada
            self.saida = saida

    def relatorio_registros(self):
        self.read_vagas()
        cursor = self.con.cursor()
        sql = 'SELECT * FROM registros_gerais'

        cursor.execute(sql)
        results = cursor.fetchall()
        if not self.quantidade_selecionada is None:
            results = list(results)
            results = results[-self.quantidade_selecionada:]
        else:
            pass
        # cursor.close()
        # self.con.close()

        diretorio = r'C:\Users\gabri\OneDrive\Área de Trabalho\relatorio_estacionamento.txt'
        self.quantidade_clientes = 0
        with open(diretorio, 'w') as novo_arquivo:
            novo_arquivo.write('Estacionamento.              Registro de clientes\n')
            novo_arquivo.write('-' * 90 + '\n')
            novo_arquivo.write('Placa       |      Concessionaria      |      Modelo        |     Cor     |    Nome \n')

            for placa, nome, modelo, cor, concessionaria, identificador in results:
                novo_arquivo.write(f'{placa:<18} {concessionaria:<26} {modelo:<20} {cor:<11}  {nome:<5} \n')
                self.quantidade_clientes += 1

            novo_arquivo.write('\n')
            novo_arquivo.write('\n')
            novo_arquivo.write(f'Quantidade de clientes: {self.quantidade_clientes}\n')

    def read_vagas(self):
        cursor = self.con.cursor()
        sql = 'SELECT * FROM vagas'
        cursor.execute(sql)
        self.results = cursor.fetchall()
        # cursor.close()
        # self.con.close()
        diretorio = r'C:\Users\gabri\OneDrive\Área de Trabalho\relatorio_VagasEstacionamento.txt'
        with open(diretorio, 'w') as novo_arquivo:
            novo_arquivo.write('Estacionamento.              Registro de clientes\n')
            novo_arquivo.write('-' * 90 + '\n')
            novo_arquivo.write('Placa       |      Concessionaria      |      Modelo        |     Cor     |    Vagas | '
                               '  Nome   \n')

            for placa, nome, modelo, cor, concessionaria, vaga in self.results:

                novo_arquivo.write(f'{placa:<20} {concessionaria:<23} {modelo:<20} {cor:<11}  {vaga:<10} {nome}\n')
        self.vagas = 0
        for _ in self.results:
            self.vagas += 1
            self.nrm_das_vagas.append(list(_)[5])

    def create(self):
        self.read_vagas()
        cursor = self.con.cursor()
        nome = self.nome
        placa = self.placa
        modelo = self.modelo
        cor = self.cor
        concessionaria = self.concessionaria
        vaga = self.vaga
        data = datetime.now()
        data_formatada = datetime.strftime(data, "%d/%m/%Y %H:%M:%S")
        read = f'SELECT * FROM registros_gerais WHERE Placa = "{self.placa}"'
        cursor.execute(read)
        results = cursor.fetchall()

        read_vaga = f'SELECT * FROM registros_de_vagas WHERE Placa = "{self.placa}"'
        cursor.execute(read_vaga)
        results_vagas = cursor.fetchall()

        if (len(placa) == 0) or (len(nome) == 0) or (len(cor) == 0) or (len(modelo) == 0) or (len(concessionaria) == 0)\
                or (len(str(vaga)) == 0):
            return
        if len(results) == 0:
            self.cliente= 'Novo Cliente'
            cadastro = f'INSERT INTO registros_gerais (Placa, Nome, Modelo, Cor, Concessionaria) VALUES ("{placa}", ' \
                  f'"{nome}", "{modelo}", "{cor}", "{concessionaria}")'

            cursor.execute(cadastro)

        if len(results_vagas) == 0:
            sql_data = f'INSERT INTO registros_de_vagas (Placa, Vaga, Data_chegada, Data_saida) VALUES ("{placa}",' \
                       f' "{vaga}",' \
                       f'"{data_formatada}", "{0}")'
        else:
            self.cliente = 'Cliente Foi adicionado so na vaga, pois ja esta cadastrado'
            sql_data = f'UPDATE registros_de_vagas SET Data_saida = "{0}", ' \
                       f'Vaga = "{vaga}", Data_chegada = "{data_formatada}"' \
                       f'WHERE Placa = "{placa}"'

        cursor.execute(sql_data)
        inserir_vaga = f'INSERT INTO vagas (Placa, Nome, Modelo, Cor, Concessionaria, Vaga) VALUES ("{placa}", "{nome}",' \
                       f'"{modelo}", "{cor}", "{concessionaria}", "{vaga}")'


        cursor.execute(inserir_vaga)

        self.con.commit()
        self.verifica = True

        self.vagas += 1
        return self.cliente

    def update(self):
        cursor = self.con.cursor()
        placa = self.placa
        nome = None
        sql = f'UPDATE vagas SET Vaga = "{nome}" WHERE Placa = "{placa}"'
        cursor.execute(sql)
        self.con.commit()


    def delete(self):
        self.read_vagas()
        cursor = self.con.cursor()
        placa = self.placa
        sql = f'DELETE FROM vagas WHERE Placa = "{placa}"'

        cursor.execute(sql)

        data = datetime.now()
        data_formatada = datetime.strftime(data, "%d/%m/%Y %H:%M:%S")

        sql_data = f'UPDATE registros_de_vagas SET Data_saida = "{data_formatada}" ' \
                   f'WHERE Placa = "{placa}"'
        cursor.execute(sql_data)
        self.con.commit()
        self.verifica = True
        self.vagas -= 1
