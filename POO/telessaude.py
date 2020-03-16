class Usuario(object):
    STATUS_LIST = ['ativo', 'inativo']
    # PERFIS = ['monitor', 'solicitante', 'teleconsultor']

    def __init__(self, ide, nome, email, cpf, dataCriacao, status):
        self.ide = ide
        self.nome = nome
        self.email = validaEmail(email)
        self.cpf = validaCPF(cpf)
        self.dataCriacao = dataCriacao
        self.status = validaStatus(status, self.STATUS_LIST)

    # def validaPerfil(self):
    #    assert self.perfil in self.PERFIS

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


# idTeleconsulta = 0


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

#    def contadorID(idTeleconsulta):
#        idTeleconsulta = idTeleconsulta + 1
#        return idTeleconsulta


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
             "ativo")
u2 = Usuario(2, "Maria", "teste@email.com", "12345678912", "13/03/2020",
             "ativo")
# print(u1, "\n", u2)


def teleConsultoria(ide, teleconsultor, solicitante, dadosCaso, dataInicio,
                    dataFim, status):
    tele = Teleconsultoria(ide, teleconsultor, solicitante, dadosCaso,
                           dataInicio, dataFim, status)
    return tele


tele1 = teleConsultoria(1, u1, u2, "febre", "01/01/2020", "02/01/2020",
                        "cancelado")
tele2 = teleConsultoria(2, u1, u2, "teste", "15/03/2020", "16/03/2020",
                        "em espera")
print(tele1, "\n", tele2)


class Unidade(object):
    STATUS_LIST = ['ativo', 'inativo']

    def __init__(self, ide, cnes, nome, municipio, uf, telefone, tipo, status):
        self.ide = ide
        self.cnes = cnes
        self.nome = nome
        self.municipio = municipio
        self.uf = uf
        self.telefone = telefone
        self.tipo = tipo
        self.status = validaStatus(status, self.STATUS_LIST)


class UsuarioUnidade(object):
    PERFIL_LIST = ['monitor', 'solicitante', 'teleconsultor']

    def __init__(self, ide, ideUsuario, ideUnidade, perfil):
        self.ide = ide
        self.ideUsuario = ideUsuario
        self.ideUnidade = ideUnidade
        self.perfil = perfil
        self.validaPerfil()

    def validaPerfil(self):
        assert self.perfil in self.PERFIL_LIST


provedora = Unidade(2, 7654321, "Provedora", "Porto Alegre", "RS",
                    "1111111111", "Telessaúde", "ativo")
consumidora = Unidade(1, 1234567, "Consumidora", "Porto Alegre", "RS",
                      "9999999999", "Unidade Básica", "ativo")
# print(unidade1)

teleconsultor = UsuarioUnidade(2, 2, 2, 'teleconsultor')
print(teleconsultor)
solicitante = UsuarioUnidade(1, 1, 1, 'solicitante')


def teleConsultoria2(ide, teleconsultor, solicitante, dadosCaso, dataInicio,
                     dataFim, status):
    tele = Teleconsultoria(ide, teleconsultor, solicitante, dadosCaso,
                           dataInicio, dataFim, status)
    return tele


teleConsultoria2(2, teleconsultor, solicitante, "Teste", "01/01/2020",
                 "02/01/2020", "em espera")
print(teleConsultoria2)
# def usuarioUnidade(idUsuario, idUnidade, perfil):
