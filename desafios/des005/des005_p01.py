nomec = str(input('Digite o seu nome completo: ')).strip()
print('O seu nome em maiúsculas é {}'.format(nomec.upper()))
print('O seu nome em minúsculas é {}'.format(nomec.lower()))
print('O seu nome tem {} letras'.format(len(nomec) - nomec.count(' ')))
print('O seu primeiro nome tem {} letras'.format(nomec.find(' ')))