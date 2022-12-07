import JoKenPo
import Par_ou_Impar
#import Operacoes

def menu():
    print('\n***********************************')
    print('*   Bem vindo ao menu de jogos!   *')
    print('* 1 - Jo Ken Po                   *')
    print('* 2 - Par ou impar                *')
    print('* 3 - Operações                   *')
    print('* 0 - Sair                        *')
    print('***********************************')

menu()

escolha = int(input('\nDigite a opção desejada: \n'))

while escolha != 0:
    if escolha == 1:
        JoKenPo.jokenpo()
    elif escolha == 2:
        Par_ou_Impar.parOuImpar()
    elif escolha == 3:
        input('Em desenvolvimento!\nPressione qualquer tecla para continuar...')
        #Operacoes.operacoes()

    menu()
    escolha = int(input('\nDigite a opção desejada: \n'))
