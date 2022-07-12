import mysql.connector


class Crudestacionamento:
    def __init__(self, placa=None, nome=None, modelo=None, cor=None, concessionaria=None, qtd_selecionada=None):
        self.placa = placa
        self.nome = nome
        self.modelo = modelo
        self.cor = cor
        self.concessionaria = concessionaria
        self.quantidade_selecionada = qtd_selecionada
        self.quantidade_clientes = None
        self.vagas = None
        self.list_clientes = None
        self.verifica = False
        self.con = mysql.connector.connect(host='localhost', user='root', password='', database='estacionamento')

        if self.con.is_connected():
            print('conectado')

    def read_registros(self):
        cursor = self.con.cursor()
        if self.placa is None:
            sql = 'SELECT * FROM registros_gerais'
        else:
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
            print(f'{placa} | {nome} | {modelo} | {cor} | {concessionaria}')

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
        results = cursor.fetchall()
        # cursor.close()
        # self.con.close()
        self.vagas = 0
        for _ in results:
            self.vagas += 1

    def create(self):
        self.read_vagas()
        cursor = self.con.cursor()
        nome = self.nome
        placa = self.placa
        modelo = self.modelo
        cor = self.cor
        concessionaria = self.concessionaria
        sql = f'SELECT * FROM registros_gerais WHERE Placa = "{self.placa}"'

        cursor.execute(sql)
        results = cursor.fetchall()

        if (len(placa) == 0) or (len(nome) == 0) or (len(cor) == 0) or (len(modelo) == 0) or (len(concessionaria) == 0):
            print(len(placa), len(nome), len(cor), len(concessionaria), len(modelo))
            return
        if len(results) == 0:

            sql = f'INSERT INTO registros_gerais (Placa, Nome, Modelo, Cor, Concessionaria) VALUES ("{placa}", ' \
                  f'"{nome}", "{modelo}", "{cor}", "{concessionaria}")'

            cursor.execute(sql)

            sql1 = f'INSERT INTO vagas (Placa, Nome, Modelo, Cor, Concessionaria) VALUES ("{placa}", "{nome}",' \
                   f'"{modelo}", "{cor}", "{concessionaria}")'
            print('Cliente novo')
        else:
            sql1 = f'INSERT INTO vagas (Placa, Nome, Modelo, Cor, Concessionaria) VALUES ("{placa}", "{nome}",' \
                   f'"{modelo}", "{cor}", "{concessionaria}")'
            print('Adicionado somente nas vagas pois ja esta registrado')

        cursor.execute(sql1)
        self.con.commit()
        self.verifica = True

        self.vagas += 1

    def update(self):
        cursor = self.con.cursor()
        placa = 'KQR-4047'
        nome = 'Gabriel Da S Rocha'
        sql = f'UPDATE registros_gerais SET Nome = "{nome}" WHERE Placa = "{placa}"'
        cursor.execute(sql)
        self.con.commit()


    def delete(self):
        self.read_vagas()
        cursor = self.con.cursor()
        placa = self.placa
        sql = f'DELETE FROM vagas WHERE Placa = "{placa}"'

        cursor.execute(sql)
        self.con.commit()
        self.verifica = True
        self.vagas -= 1


'''if __name__ == '__main__':
    test = Crudestacionamento()
    test.create()'''
