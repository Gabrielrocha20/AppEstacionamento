import sys
from BancoDoEstacionamento.CRUD import Crudestacionamento
from interface import *
from PyQt5.QtWidgets import QMainWindow, QApplication


class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.funcao = Crudestacionamento()
        self.funcao.read_vagas()
        self.qtd_vagas = int(self.funcao.vagas)

        self.maximo_vaga = 10

        # Butons
        self.btnNumeroDeVagas.clicked.connect(self.nrm_vagas)
        self.btnGerarRelatorio.clicked.connect(self.gerar)
        self.btnBuscarCarro.clicked.connect(self.buscar)
        self.btnAdicionar.clicked.connect(self.adicionar)
        self.btnExcluir.clicked.connect(self.excluir)
        self.btnReset.clicked.connect(self.resetar)
        self.btnVerVagas.clicked.connect(self.mostrar_vagas_ocupadas)

    def nrm_vagas(self):
        nrm = self.spinNumeroDeVagas.text()
        self.maximo_vaga = int(nrm)
        self.labelVagas.setText(f'{self.qtd_vagas}/{self.maximo_vaga}')

    def gerar(self):
        quantidade = self.spinQuantidade.text()
        gerar_relatorio = Crudestacionamento(qtd_selecionada=int(quantidade))
        gerar_relatorio.relatorio_registros()

        with open(r'../../relatorio_estacionamento.txt', 'r') as relatorio:
            self.labelestacionamento.setText(relatorio.read())

    def mostrar_vagas_ocupadas(self):
        ver = Crudestacionamento()
        ver.read_vagas()

        with open(r'../../relatorio_Vagasestacionamento.txt', 'r') as relatorio:
            self.labelestacionamento.setText(f'{relatorio.read()}\n'
                                             f'\n'
                                             f'\n'
                                             f'Pré vizualização(O arquivo foi enviado para sua aréa de trabalho'
                                             f'relatorio_VagasEstacionamento.txt)')

    def buscar(self):
        placa = self.inputPlaca.text()

        busca_cliente = Crudestacionamento(placa)
        busca_cliente.read_registros()

        nome = busca_cliente.nome
        cor = busca_cliente.cor
        modelo = busca_cliente.modelo
        concessionaria = busca_cliente.concessionaria
        if (placa is None) or (nome is None) or (cor is None) or (modelo is None) or (concessionaria is None):
            self.labelestacionamento.setText('Não encontrado')
        else:
            self.labelestacionamento.setText(f'Placa     |   Concessionaria    |   Modelo     |     Cor     |    Nome\n'
                                             f'{placa:<11} {concessionaria:<24} {modelo:<17} {cor:<11} {nome:<5} \n')

    def adicionar(self):
        vagas = Crudestacionamento()
        vagas.read_vagas()
        lista_vagas_ocupadas = vagas.nrm_das_vagas
        lista_maximo_vagas = []
        for mv in range(1, 1 + self.maximo_vaga):
            lista_maximo_vagas.append(mv)
        if self.qtd_vagas == self.maximo_vaga:
            return self.labelestacionamento.setText('Estacionamento Cheio')
        vagas_livre = [elemento for elemento in lista_maximo_vagas if not elemento in lista_vagas_ocupadas]
        vaga = vagas_livre[0]
        placa = self.inputPlaca.text()
        nome = self.inputNome.text()
        cor = self.inputCor.text()
        modelo = self.inputModelo.text()
        concessionaria = self.inputConcessionaria.text()

        ver_vagas = Crudestacionamento(placa=placa, nome=nome, modelo=modelo, cor=cor,
                                       concessionaria=concessionaria, vaga=vaga)
        ver_vagas.create()

        if (len(placa) == 0) or (len(nome) == 0) or (len(cor) == 0) or (len(modelo) == 0) or (len(concessionaria) == 0):
            self.labelVerificaAdicionado.setText("")
            return self.labelVerificaExluido.setText('Erro')
        elif ver_vagas.verifica is True:
            self.labelVerificaExluido.setText("")
            self.labelestacionamento.setText(f'Placa   |   Concessionaria    |   Modelo     |     Cor     |    Nome \n'
                                             f'{placa:<11} {concessionaria:<21} {modelo:<16} {cor:<11}  {nome:<5} \n'
                                             f'\n'
                                             f'Adicionado na vaga {vaga}\n'
                                             f'{ver_vagas.cliente}')

            self.labelVerificaAdicionado.setText('Adicionado')
        self.qtd_vagas = ver_vagas.vagas
        self.labelVagas.setText(f'{self.qtd_vagas}/{self.maximo_vaga}')

    def excluir(self):
        placa = self.inputPlaca.text()

        cliente_saindo = Crudestacionamento(placa)
        cliente_saindo.read_registros()

        cliente_saindo.delete()
        self.qtd_vagas = cliente_saindo.vagas

        self.labelVerificaExluido.setText("Excluido")
        self.labelVagas.setText(f'{self.qtd_vagas}/{self.maximo_vaga}')

    def resetar(self):
        self.inputPlaca.setText("")
        self.inputNome.setText("")
        self.inputCor.setText("")
        self.inputModelo.setText("")
        self.inputConcessionaria.setText("")
        self.labelVerificaAdicionado.setText("")
        self.labelVerificaExluido.setText("")
        self.spinQuantidade.setValue(0)
        self.labelestacionamento.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    estacionamento = Interface()
    estacionamento.show()
    app.exec()