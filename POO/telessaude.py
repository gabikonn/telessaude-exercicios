class Usuario(object):
    STATUS_LIST = ['ativo', 'inativo']
    PERFIS = ['monitor', 'solicitante', 'teleconsultor']

    def __init__(self, ide, nome, email, cpf, dataCriacao, status, perfil):
        self.ide = ide
        self.nome = nome
        self.email = validaEmail(email)
        self.cpf = validaCPF(cpf)
        self.dataCriacao = dataCriacao
        self.status = validaStatus(status, self.STATUS_LIST)
        self.perfil = perfil
        self.validaPerfil()

    def validaPerfil(self):
        assert self.perfil in self.PERFIS

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Teleconsultoria(object):
    STATUS_LIST = ['em espera', 'em atendimento', 'finalizado', 'cancelado']

    def __init__(self, ide, teleconsultor, solicitante, dadosCaso, dataInicio,
                 dataFim, status):
        self.ide = ide
        self.teleconsultor = teleconsultor
        self.solicitante = solicitante
        self.dadosCaso = dadosCaso
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.status = validaStatus(status, self.STATUS_LIST)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


def validaStatus(status, status_arr=[]):
    assert status in status_arr
    return status


def validaCPF(cpf):
    assert len(cpf) == 11
    return "%s.%s.%s-%s" % (cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])


def validaEmail(email):
    a = email.find("@")
    b = email.find(".")
    assert a != -1 and (a < b)
    return email


u1 = Usuario(1, "Gabi", "blabla@email.com", "03944319010", "13/03/2020",
             "ativo", "teleconsultor")
u2 = Usuario(2, "Maria", "teste@email.com", "12345678912", "13/03/2020",
             "ativo", perfil="solicitante")
print(u1, "\n", u2)

tele = Teleconsultoria(1, u1, u2, "febre", "13/02/2020",
                       "25/02/2020", "em espera")
print(tele)
print(tele.teleconsultor.nome)

# def teleconsultoria(teleconsultor, solicitante):
