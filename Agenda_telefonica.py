class Endereco:
    def __init__(self, rua, casa, municipio, provincia, pais):
        self.rua = rua
        self.casa = casa
        self.municipio = municipio
        self.provincia = provincia
        self.pais = pais

class Contato:
    def __init__(self, nome, telefone, email, endereco, bi=None, nif=None):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.bi = bi
        self.nif = nif

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def editar_contato(self, nome, novo_contato):
        for i, contato in enumerate(self.contatos):
            if contato.nome == nome:
                self.contatos[i] = novo_contato
                break

    def remover_contato (self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)

    def buscar_contato_por_nome(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None

    def buscar_contato_por_telefone(self, telefone):
        for contato in self.contatos:
            if contato.telefone == telefone:
                return contato
        return None
endereco1 = Endereco("Rua da Orla Maritima", 1234, "Vila de Cacuaco", "Provincia Luanda", "País Angola")
contato1 = Contato("Joao Augusto", "932898270","johnnguifa6@gmail.com", endereco1, bi="008356715BO041")
agenda = Agenda()
agenda.adicionar_contato(contato1)

contato_encontrado = agenda.buscar_contato_por_nome("Joao Augusto")
print("numero e nome", contato_encontrado.nome, contato_encontrado.telefone)

contato_encontrado = agenda.buscar_contato_por_nome("Joao Augusto")
print(contato_encontrado.endereco.rua)
novo_contato=(input("Informe um novo contacto\n"))
novo_endereco=(input("Informe o novo endereço\n"))
print("novo contato adicionado",novo_contato)
print("Endero indicado:",novo_endereco, )