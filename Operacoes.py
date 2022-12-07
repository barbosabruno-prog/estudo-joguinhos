'''  OPERAÇÕES: O USUÁRIO ESCOLHE A OPERAÇÃO QUE DESEJA OU ESCOLHE OPERAÇÕES ALEATÓRIAS.
     SÃO 10 QUESTÕES NO TOTAL. AO FINAL O USUÁRIO RECEBE A NOTA '''

def operacoes():

    import random

    oprc = {1:'adc_sub', 2:'adc_sub', 3:'mult', 4:'div', 5:'Mix'}

    def adc_sub(op):
        for i in range(10):

            t1 = random.randint(1, 999)
            t2 = random.randint(1, 999)

            resp = int(input('{} {} {}'.format(t1, op, t2)))

            certos = 0
            errados = 0

            if op == '+':
                resul = t1 + t2
            else:
                resul = t1 - t2

            if resp == resul:
                certos += 1
            else:
                errados += 1




    def mult():

    def div():







        comeco = input('Novo jogo? (S/N) ')

        while comeco.lower() == 's':

            playerChoice = int(input('Escolha a operação desejada\n '
                                     '1 = Adição | 2 = Subtração | 3 = Multiplicação | 4 = Divisão | 5 = Mix \n'))

            if playerChoice < 1 or playerChoice > 5:
                print('Não é uma opção válida!!!\n')
                continue

            print('Sua escolha: {}'.format(oprc[playerChoice]))




            comeco = input('\nDeseja jogar outra vez? (S/N) ')
            if comeco.lower() == 's':
                print('\n********************************\n')


    operacoes()