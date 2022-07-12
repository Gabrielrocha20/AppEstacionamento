from BancoDoEstacionamento.CRUD import Crudestacionamento

placa = ['JGI-0570', 'MZQ-9882', 'LNG-1706', 'NEQ-8282', 'IAL-8087', 'NAC-1482', 'KOC-4054', 'APZ-0104']
nome = ['Miguel', 'Rafael', 'Samuel', 'Lucas', 'Emanuel', 'Monique', 'Eduarda', 'Maria']
sobrenome1 = ['Da Silva', 'Dos santos', 'Da cruz', 'De Souza']
sobrenome2 = ['Fernandes', 'Oliveira', 'Rocha', 'Domingues']
modelo = ['ONIX', 'CRUZE', 'EQUINOX', 'TRACKER', 'BOLT EV', 'CAMARO', 'S10 HIGH COUNTRY', 'SPIN']
cor = ['branco', 'preto', 'vermelho', 'laranja', 'azul']
concessionaria = ['chevrolet']

if __name__ == '__main__':
    test = Crudestacionamento(placa[7], f'{nome[7]} {sobrenome1[3]} {sobrenome2[0]}',
                              modelo[7], cor[3], concessionaria[0])
    test.create()

