from controle.controlador_integrante import ControladorIntegrante
from limite.tela_participante import TelaParticipante


class ControladorParticipante(ControladorIntegrante):

    def __init__(self, controlador_sistema, controlador_pessoa):
        super().__init__(controlador_sistema, controlador_pessoa, TelaParticipante(self))

    def abrir_menu_visualizacao(self, participante):

        opcoes = {1: self.alterar, 2: self.remover,
                  3: self.mostrar_vacinas, 4: self.mostrar_exames}

        menu = self.tela.mostrar_menu_visualizacao

        self.abrir_menu(menu, opcoes,  participante)

    def mostrar_vacinas(self, participante):

        cartao = participante.cartao_de_vacina

        self.controlador_sistema.controlador_cartao_de_vacina.mostrar(cartao)

    def registrar_exame(self, participante):

        novo_exame = self.controlador_sistema.controlador_exame.cadastrar()
        
        if(participante.nascimento > novo_exame.data):
            raise ValueError("O exame não pode ser realizado antes do nascimento do participante.")

        participante.add_exame(novo_exame)
        self.controlador_sistema.controlador_exame.listar(
            participante.exames)

    def mostrar_exames(self, participante):

        self.controlador_sistema.controlador_exame.mostrar(
            participante.exames, lambda: self.registrar_exame(participante))
