usuario = 'Angelo'
senha = 'Angelo123'
    
def Login():
    print("Digite seu usuario")
    userDigitado = input(">:")
    print("Digite sua senha")
    pwdDigitado = input(">:")
    if userDigitado == usuario and pwdDigitado == senha:
        print("Acesso Liberado")
    else:
        print("Acesso Negado")

Login()

