from BancoDoEstacionamento.CRUD import Crudestacionamento


class Estacionamento:
    def __init__(self, placa=None):
        self.vagas = 10
        self.placa = placa

    def adicionar_carro_na_vaga(self):
        ver_vagas = Crudestacionamento()
        ver_vagas.read_vagas()

        if ver_vagas.vagas >= self.vagas:
            print(f'O estacionamenta esta CHEIO {ver_vagas.vagas}/{self.vagas}')
        else:
            print(f'Vagas {ver_vagas.vagas}/{self.vagas}')

    def excluir_carro_da_vaga(self):
        cliente_saindo = Crudestacionamento(self.placa)
        cliente_saindo.delete()
        cliente_saindo.read_vagas()
        print(f'{cliente_saindo.vagas}/{self.vagas} vagas')

    def gerar_relatorio(self):
        ver_vagas = Crudestacionamento()
        ver_vagas.relatorio_registros()

    def informar_vagas(self):
        ver_vagas = Crudestacionamento()
        ver_vagas.read_vagas()
        print(f'Vagas {ver_vagas.vagas}/{self.vagas}')

    def busca_carro(self):
        buscar_informacao = Crudestacionamento('KNE-6671')
        buscar_informacao.read_registros()


'''if __name__ == '__main__':
    test = Estacionamento('MUV-2457')
    test.excluir_carro_da_vaga()'''