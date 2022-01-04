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