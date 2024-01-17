print("===============================================================================================")
print("                                            AGENDA TELEFÓNICA                                    ")
print("===============================================================================================\n")
class Endereco:
    def __init__(self, rua, casa, municipio, provincia, pais):
        self.rua = rua
        self.casa = casa
        self.municipio = municipio
        self.provincia = provincia
        self.pais = pais

class Contato:
    def __init__(self, nome, telefone, email, bi, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.bi = bi
        self.endereco = endereco

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def editar_contato(self, nome, novo_contato):
        for i in range(len(self.contatos)):
            if self.contatos[i].nome == nome:
                self.contatos[i] = novo_contato
                break

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                break

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

def menu_inicial():
    print("Apresentamos-lhe a agenda telefonica | Escolha as opções abaixos para começar a usar\n")
    print("1. Adicionar contato")
    print("2. Editar contato")
    print("3. Remover contato")
    print("4. Buscar contato por nome")
    print("5. Buscar contato por telefone")
    print("6. Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao

# Exemplo de uso do menu
agenda = Agenda()
while True:
    opcao = menu_inicial()
    if opcao == 1:
        # Adicionar contato
        nome = input("Nome do contato: ")
        telefone = input("Telefone do contato: ")
        email = input("Email do contato: ")
        bi=input("BI ")
        rua = input("Rua: ")
        casa = input("Casa: ")
        municipio = input("Município: ")
        provincia = input("Província: ")
        pais = input("País: ")
        endereco = Endereco(rua, casa, municipio, provincia, pais)
        novo_contato = Contato(nome, telefone, email, bi, endereco)
        agenda.adicionar_contato(novo_contato)
    elif opcao == 2:
        # Editar contato
        nome = input("Nome do contato a ser editado: ")
        novo_nome = input("Novo nome do contato: ")
        novo_telefone = input("Novo telefone do contato: ")
        novo_email = input("Novo email do contato: ")
        novo_rua = input("Nova rua: ")
        novo_casa = input("Nova casa: ")
        novo_bi=input("Novo BI ")
        novo_municipio = input("Novo município: ")
        novo_provincia = input("Nova província: ")
        novo_pais = input("Novo país: ")
        novo_endereco = Endereco(novo_rua, novo_casa, novo_municipio, novo_provincia, novo_pais)
        novo_contato = Contato(novo_nome, novo_telefone, novo_email, novo_endereco)
        agenda.editar_contato(nome, novo_contato)
    elif opcao == 3:
        # Remover contato
        nome = input("Nome do contato a ser removido: ")
        agenda.remover_contato(nome)
    elif opcao == 4:
        # Buscar contato com o nome
        nome = input("Nome do contato a ser buscado: ")
        contato_encontrado = agenda.buscar_contato_por_nome(nome)
        if contato_encontrado:
            print(f"Contato encontrado: {contato_encontrado.nome} - {contato_encontrado.telefone}")
        else:
            print("Contato não encontrado")
    elif opcao == 5:
        # Buscar contato com nª de telefone
        telefone = input("Telefone do contato a ser buscado: ")
        contato_encontrado = agenda.buscar_contato_por_telefone(telefone)
        if contato_encontrado:
            print(f"Contato encontrado: {contato_encontrado.nome} - {contato_encontrado.telefone}")
        else:
            print("Contato não encontrado")
    elif opcao == 6:
        # para finalizar o programa
        break
    else:
        print