from entidade.participante import Participante
from entidade.endereco import Endereco
from controle.controlador import Controlador
from limite.tela_participante import TelaParticipante


class ControladorParticipante(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaParticipante(self))

    def abrir_menu_inicial(self):

        opcoes = {1: self.cadastrar, 2: self.listar, 3: self.ver_detalhes}
        opcoes_validas = [0, 1, 2, 3]
        menu = self.tela.mostrar_menu_inicial

        self.listar()
        self.abrir_menu(menu, opcoes, opcoes_validas)

    def cadastrar(self):

        dados = self.tela.mostrar_tela_cadastro()

        try:
            # Procurar se há participante com o cpf
            for participante in self.entidades:
                if(participante.cpf == dados["cpf"]):
                    raise ValueError
        except ValueError:
            self.tela.mostrar_mensagem(
                "Erro: Já existe um participante cadastrado com esse CPF.")
        else:

            # criar participante
            novo_participante = Participante(
                dados["cpf"], dados["nome"], dados["nascimento"], dados["endereco"])

            # incluir participante
            self.entidades.append(novo_participante)
            self.tela.mostrar_mensagem("Participante cadastrado com sucesso")
            self.listar()

    def alterar(self, participante):

        dados = self.tela.mostrar_tela_cadastro(alterar=True)

        participante.nome = dados["nome"]
        participante.cpf = dados["cpf"]
        participante.nascimento = dados["nascimento"]
        participante.endereco = dados["endereco"]

        self.tela.mostrar_detalhes(participante)

    def remover(self, participante):
        # first version
        # Later, add verification for events that have the participante listed

        confirmacao = self.tela.confirmar()
        if(confirmacao):
            self.entidades.remove(participante)
