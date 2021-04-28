import re

class validador:
    def validarNome(nome):
        pattern = re.compile("^[a-zA-Z .]{3,30}$")
        if re.match(pattern, nome):
            return True   
        return False

    def validarEmail(email):
        pattern = re.compile("^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$")
        if re.match(pattern, email):
            return True
        return False

    def validarSenha(senha):
        pattern = re.compile("^.{4,32}$")
        if re.match(pattern, senha):
            return True
        return False