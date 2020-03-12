class Usuario:
    def __init__(self, ide, nome, email, cpf, dataCriacao, status, perfil):
        self.ide = ide
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.dataCriacao = dataCriacao
        self.status = status
        self.perfil = perfil

class Teleconsultoria:
    def __init__(self, ide, teleconsultor, solicitante, dadosCaso, dataInicio, dataFim, status):
        
