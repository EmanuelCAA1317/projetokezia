class Usuario:

    def __init__(self, email, senha, nome, sexo, idade, peso, altura, objetivo, nivelAtividade) :
        self.email = email
        self.senha = senha
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.imc = peso/(altura*altura)
        self.objetivo = objetivo #manter, aumentar ou diminuir peso
        self.nivelAtividade = nivelAtividade # sedentario, moderado, muito ativo
        self.dieta = self.geraQuantitativoDieta(sexo, idade, peso, altura,nivelAtividade)
        self.historico = [] # armazena os dados necessários para gerar um gráfico de desempnho em relação a peso, imc

    def getemail(self):
        return self.email

    def setemail(self,email):
        self.email = email

    def getSenha(self):
        return self.senha

    def setSenha(self,senha):
        self.senha = senha

    def getNome(self):
        return self.nome

    def setNome(self,nome):
        self.nome = nome

    def getSexo(self):
        return self.sexo

    def setSexo(self,sexo):
        self.sexo = sexo

    def getIdade(self):
        return self.idade

    def setIdade(self,idade):
        self.idade = idade

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    def geraQuantitativoDieta(self, sexo, idade, peso, altura, objetivo, nivelAtividade):
        #c código de condicionais para definir a quantidade de gordura, proteina, carboidrato e agua
        pass
