from controle.controlador_integrante import ControladorIntegrante
from limite.tela_participante import TelaParticipante


class ControladorParticipante(ControladorIntegrante):

    def __init__(self, controlador_sistema, controlador_pessoa):
        super().__init__(controlador_sistema, controlador_pessoa, TelaParticipante(self))

    def abrir_menu_visualizacao(self, participante):

        opcoes = {1: self.alterar, 2: self.remover,
                  3: self.mostrar_vacinas, 4: self.mostrar_exame}

        menu = self.tela.mostrar_menu_visualizacao

        self.abrir_menu(menu, opcoes,  participante)

    def mostrar_vacinas(self, participante):

        cartao = participante.cartao_de_vacina

        self.controlador_sistema.controlador_cartao_de_vacina.mostrar(cartao)

    def registrar_exame(self, participante):

        participante.exame = self.controlador_sistema.controlador_exame.cadastrar()

    def mostrar_exame(self, participante):
        # the lambda function is a workaround for now. Not liking this solution.
        try:
            self.controlador_sistema.controlador_exame.mostrar(
                participante.exame, lambda: self.registrar_exame(participante))
        except AttributeError as err:
            print(err)
            registrar = self.tela.mostrar_tela_erro_exame()
            if(registrar):
                self.registrar_exame(participante)

    def incluir(self, pessoa):
        if(pessoa in self.entidades):
            raise ValueError("A pessoa indicada já está cadastrada!")

        cartao_de_vacina = self.controlador_sistema.controlador_cartao_de_vacina.cadastrar()

        self.entidades.append(pessoa)
        self.tela.mostrar_mensagem("Cadastro realizado com sucesso")
        self.ver_todos()
