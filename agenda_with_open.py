agenda = []
nome_arquivo = 'contatos'
try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linhas in arquivo.readlines():
            nome, telefone = linhas.strip().split('#')
            agenda.append([nome, telefone])
except:
    with open(nome_arquivo, 'x', encoding='utf-8') as arquivo:
        pass

def pede_nome():
    return input('Nome: ')


def pede_telefone():
    return input('Telefone: ')


def mostra_dados(nome, telefone):
    print(f'Nome: {nome} Telefone: {telefone}')


def pede_nome_arquivo():
    return input('Nome do Arquivo: ')


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
        else:
            pass
    return None


def altera():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print('Encontrado:')
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
        grava()
    else:
        print('Nome não encontrado.')



def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])
    grava()


def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
        grava()
    else:
        print('Nome não encontrado.')


def lista():
    print('\nAgenda\nn------------------------------')
    for e in agenda:
        mostra_dados(e[0], e[1])


def grava():
    nome_arquivo = 'contatos'
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for e in agenda:
            arquivo.write(f'{e[0]}#{e[1]}\n')


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor and valor <= fim:
                return valor
            else:
                print(f'Valor inválido, favor digitar entre {inicio} e {fim}')
        except:
            print(f'Valor inválido, favor digitar entre {inicio} e {fim}')


def menu():
    print('''
    1 - Novo
    2 - Alterar
    3 - Apagar
    4 - Listar


    0 - Sair
    ''')
    return valida_faixa_inteiro('Escolha uma opcao: ', 0, 4)


while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()