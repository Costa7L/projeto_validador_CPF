cpf = input('digite o CPF: ')

cpf = cpf.replace(' ', '')
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')

if len(cpf) != 11 or not cpf.isdigit():
    print('CPF inválido!')

elif cpf == cpf[0] * 11:
    print('CPF inválido!')

else:

    soma = 0
    peso = 10

    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    digito1 = (soma * 10) % 11

    if digito1 >= 10:
        digito1 = 0

    soma = 0
    peso = 11

    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    digito2 = (soma * 10) % 11

    if digito2 == 10:
        digito2 = 0

    if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
        print('CPF válido!')
        print(f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
    else:
        print('CPF inválido!')
