def PrintName(name, lastname):
    #nameFormat = '{} {}'.format(name.capitalize(), lastname.capitalize())
    nameFormat = f'{name.capitalize()} {lastname.capitalize()}'
    print(nameFormat)

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
PrintName(nome, sobrenome)