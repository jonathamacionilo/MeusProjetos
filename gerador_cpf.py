import random
import sys
import re
import time


while True:
    opcao = input('[1]Validar CPF [2]Gerar CPF [3]Encerrar: ')
    
    # Encerrar programa
    if opcao == '3':
        print('Encerrando programa...')
        time.sleep(1.5)
        print('Programa encerrado!')
        sys.exit()
    # Validar CPF do usuário
    elif opcao == '1':
        cpf_nao_tratado = input('Digite o CPF: ')

        # tratando entrada do usuário, extraindo apenas números
        cpf_tratado = re.sub(r'[^0-9]', '', cpf_nao_tratado) 
        nove_digitos = cpf_tratado[:9]
        contador_regressivo_1 = 10

        # tratando entrada do usuário, valores repetidos ex.: 11111111111
        entrada_sequencial = cpf_tratado == \
            cpf_tratado[0] * len(cpf_tratado)
            
        if entrada_sequencial:
            print('Dados sequenciais. Informe um número válido!\n')
            continue
            
        # calculo do primeiro digito verificador
        resultado_digito_1 = 0
        for digito in nove_digitos:
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        # Calculo do segundo digito verificador
        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11

        resultado_digito_2 = 0
        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        # Verificação / validação do CPF
        cpf_calculado = f'{nove_digitos}{digito_1}{digito_2}'

        if cpf_calculado == cpf_tratado:
            print(f'CPF: {cpf_tratado} é válido.\n')
        else:
            print(f'CPF: {cpf_tratado} é INVÁLIDO\n')
    # Gerador randomico de CPF válido
    elif opcao == '2':
        random_nove = ''
        for i in range(9):
            random_nove += str(random.randint(0, 9))

        contador_regressivo_1 = 10
        
        # calculo do primeiro digito verificador
        resultado_digito_1 = 0
        for digito in random_nove:
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        # Calculo do seungo digito verificador
        dez_digitos = random_nove + str(digito_1)
        contador_regressivo_2 = 11

        resultado_digito_2 = 0
        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        # Verificação / validação do CPF
        cpf_calculado = f'{random_nove}{digito_1}{digito_2}'
        print(f'CPF gerado: {cpf_calculado}\n')
