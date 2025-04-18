from time import sleep
from random import randint
jogador = int(input('Escolha: \n [ 1 ] pedra \n [ 2 ]  papel \n [ 3 ]  tesoura \n ->'))

if jogador not in (1, 2, 3):
    print('Jogada Inválida!!')
else:
    compu = randint(1, 3)

    print('JO')
    sleep(1)
    print(' KEN')
    sleep(1)
    print('  PO!!!')
    sleep(1)

    print('\033[1;33m---======---====---====-----=====\033[0m')
    opcoes = {1: 'pedra', 2: 'papel', 3: 'tesoura'}
    print('\033[34mO jogador escolheu:\033[0m',opcoes[jogador])
    print('\033[35mA máquina escolheu:\033[0m',opcoes[compu])
    print('\033[1;33m---======---====---====-----=====\033[0m')

    if jogador == 1 and compu == 2 or jogador == 2  and compu == 3 or jogador == 3 and compu == 1:
      print('\033[31mA máquina venceu!!!\033[0m')
    elif jogador == compu:
      print('\033[1;37m Empate!!\033[0m')
    else:
      print('\033[1;32mO jogador veneceu!!heheehh\033[0m')