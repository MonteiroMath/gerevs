import PySimpleGUI as sg
from abc import ABC, abstractmethod
from limite.tela import Tela


class TelaIntegrante(Tela, ABC):

    @abstractmethod
    def __init__(self, controlador):

        super().__init__(controlador)

    def init_menu_inicial(self, entidades):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Menu Inicial",
                     size=(30, 1), font=("Helvetica", 25))],
            [sg.Table([[entidade["nome"], entidade["cpf"], entidade["nascimento"].strftime("%d/%m/%Y")] for entidade in entidades],  headings=["Nome", "CPF",
                      "Nascimento"], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
            [sg.Button("Cadastrar", key=1), sg.Button("Alterar", key=2), sg.Button("Remover", key=4), sg.Button(
                "Ver Detalhes", key=3), sg.Button("Voltar", key=0)]
        ]

        self.window = sg.Window(
            "Menu Inicial", default_element_size=(40, 1)).Layout(layout)

    def init_detalhes(self, pessoa):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Nome: ", size=(15, 1)), sg.Text(pessoa["nome"])],
            [sg.Text("CPF: ", size=(15, 1)), sg.Text(pessoa["cpf"])],
            [sg.Text("Nascimento: ", size=(15, 1)),
             sg.Text(pessoa["nascimento"].strftime("%d/%m/%Y"))],
            [sg.Ok()]
        ]

        self.window = sg.Window(
            "Detalhes", default_element_size=(40, 1)).Layout(layout)

    def mostrar_menu_inicial(self, entidades):
        self.init_menu_inicial(entidades)
        button, values = self.open()
        self.close()
        return button, values

    def mostrar(self, pessoa, i):
        print(i, pessoa)

    def mostrar_detalhes(self, pessoa):
        self.init_detalhes(pessoa)
        self.open()
