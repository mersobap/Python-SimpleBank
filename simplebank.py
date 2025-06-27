# Variáveis de base
saldo = 0
limite = 500
num_saques = 0
LIMITE_SAQUES = 3

operacoes = []
tpOper = ['Depósito','  Saque','Saldo Atual']

menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
\n==> """
    
def Formata(valor, tp):
    tipo = tpOper[tp]
    return f'{tipo}:\tR$ {valor:.2f}'


# Programa principal
opcao = ''
while (opcao != 'q'):
    opcao = input(menu)
    
    if opcao == 'd':
        print('Depósito')
        # Procedimento para depósito
        valor = float(input('Qual é o valor a depositar? '))
        if valor > 0:
            saldo += valor
            operacoes.append(Formata(valor, 0))
        else:
            print('Valor inválido! Não existe depósito negativo!')
        
    elif opcao == 's':
        print('Saque')
        # Procedimento para saque
        valor = float(input('Qual é o valor a depositar? '))
        # Verificações
        ver_saldo = valor > saldo
        ver_limite = valor > limite
        ver_excede = num_saques >= LIMITE_SAQUES

        if ver_saldo:
            print('Operação falhou! Não há saldo suficiente!')

        elif ver_limite:
            print('Operação falhou! Valor excede limite de valor diário!')

        elif ver_excede:
            print('Operação falhou! Excedido o número de operações diárias!')

        elif valor > 0:
            saldo -= valor
            operacoes.append(Formata(valor, 1))
            num_saques += 1

        else:
            print('Operação falhou! Valor inválido!')
        
    elif opcao == 'e':
        print('\n========== Extrato ==========\n')
        # Procedimento para extrato
        if len(operacoes) == 0:
            print('Não foram realizadas operações!')
        else:
            for l in operacoes:
                print(l)
            print(Formata(saldo, 2))
        print('\n=============================\n')
        
    elif opcao == 'q':
        # sair do sistema
        print('Sair')
    else:
        print('Operação inválida! Selecione uma das opções de menu!\n')
