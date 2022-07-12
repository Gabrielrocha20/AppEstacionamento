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
        self.qtd_vagas = self.funcao.vagas

        self.spinQuantidade.setMaximum(10)
        self.maximo_vaga = 10
        self.labelVagas.setText(f'{self.qtd_vagas}/{10}')

        # Butons
        self.btnGerarRelatorio.clicked.connect(self.gerar)
        self.btnBuscarCarro.clicked.connect(self.buscar)
        self.btnAdicionar.clicked.connect(self.adicionar)
        self.btnExcluir.clicked.connect(self.excluir)
        self.btnReset.clicked.connect(self.resetar)

    def gerar(self):
        quantidade = self.spinQuantidade.text()
        gerar_relatorio = Crudestacionamento(qtd_selecionada=int(quantidade))
        gerar_relatorio.relatorio_registros()

        with open(r'../../relatorio_estacionamento.txt', 'r') as relatorio:
            self.labelestacionamento.setText(relatorio.read())

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
        placa = self.inputPlaca.text()
        nome = self.inputNome.text()
        cor = self.inputCor.text()
        modelo = self.inputModelo.text()
        concessionaria = self.inputConcessionaria.text()
        if self.qtd_vagas == 10:
            return self.labelestacionamento.setText('Estacionamento Cheio')
        else:
            ver_vagas = Crudestacionamento(placa=placa, nome=nome, modelo=modelo, cor=cor, concessionaria=concessionaria)
            ver_vagas.create()

        if (len(placa) == 0) or (len(nome) == 0) or (len(cor) == 0) or (len(modelo) == 0) or (len(concessionaria) == 0):
            self.labelVerificaAdicionado.setText("")
            return self.labelVerificaExluido.setText('Erro')
        elif ver_vagas.verifica is True:
            self.labelVerificaExluido.setText("")
            self.labelestacionamento.setText(f'Placa   |   Concessionaria    |   Modelo     |     Cor     |    Nome \n'
                                             f'{placa:<11} {concessionaria:<21} {modelo:<16} {cor:<11}  {nome:<5} \n')

            self.labelVerificaAdicionado.setText('Adicionado')
        self.qtd_vagas = ver_vagas.vagas
        self.labelVagas.setText(f'{self.qtd_vagas}/{10}')

    def excluir(self):
        placa = self.inputPlaca.text()

        cliente_saindo = Crudestacionamento(placa)
        cliente_saindo.read_registros()

        cliente_saindo.delete()
        self.qtd_vagas = cliente_saindo.vagas

        self.labelVerificaExluido.setText("Excluido")
        self.labelVagas.setText(f'{self.qtd_vagas}/{10}')

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