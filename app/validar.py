import re
from home.consultas import consulta

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

    def validarDinheiro(value):
        pattern = re.compile("^[1-9]\d{0,2}(\.\d{3})*,\d{2}$")
        if re.match(pattern, value):
            return True
        return False
    
    def filtrarDinheiro(value):
        return float(re.sub(r"\D", "", value)) / 100
        
    def validarTipo(type_id):
        pattern = re.compile("^([1-2])$")
        if re.match(pattern, type_id):
            return True
        return False
    
    def validarCat(cat_id):
        pattern = re.compile("^[+]?[0-9]+$")
        if re.match(pattern, cat_id):
            return True
        return False