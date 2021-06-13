#UNN0280104NNA

#JOSÉ BRAGA MALVEIRA 03112555
#MARCOS ANTONIO DE OLIVEIRA 03118560
#JULLY ANNE DA SILVA MARAES 03176476
'''faz a verificação das informações aí sim esse menu de transações
Coloca o cartão no leitor após a leitura a máquina vai pedir a biometria e caso o cliente não consiga através da biometria e após três erros de biometria aí ele pega a senha eletrônica.
o cliente aperta na opção saque e depois o valor desejado a máquina faz a verificação de saldo na conta, aí o sistema pede novamente a senha númerica para confirmar o saque.
Aí a máquina pede para o cliente retirar o cartão aí o processo se encerra se o cliente quiser fazer nova operação insere o cartão novamente aí sistema vai pedir a senha biometria e depois de 3 erros a senha numerica
1 erro do processo que eu coloquei a BIOMETRIA
2 senha para confirmar o saque
3 caso o cliente faça um novo processo a senha deverá ser exigida novamente'''



'''caixa eletronico'''

menu = 0
print('''MENU
(1) SACAR
(2) SALDO
(3) OPERAÇÃO SEM CARTÃO''')




opção = float(input('qual sua opção?'))
if opção == 3:
    print('''MENU
    (1) SACAR
    (2) SALDO''')




elif opção == 2:
    print('insira o cartão')
    terminal = str('insira o cartão')
    meu = str(input('escolha seu banco'))
    if terminal != meu:
        print('voçê está no banco {}'.format(meu))
        bio = input('ja cadastrou sua biometria?')
        bio_senha = bio
    saldo = float(input('saldo'))
    print('seu saldo atual é de R${}'.format(saldo))


elif opção == 1:

    print('insira o cartão')
    terminal = str('insira o cartão')
    meu = str(input('escolha seu banco'))
    saldo = float(input('saldo'))
    if terminal != meu:
        print('voçê está no banco {}'.format(meu))
        bio = input('ja cadastrou sua biometria?')
        bio_senha = bio

        print('qual o valor q deseja sacar?')
        vlsaque = int(input('digite o valor que deseja sacar'))
        if vlsaque <= saldo:
            print('insira novamente sua senha ou biometria')
            input(bio_senha)
            print('retire o valor de R${}'.format(vlsaque))
        else:
            print('SALDO INSUFUCIENTE R${}'.format(saldo))















