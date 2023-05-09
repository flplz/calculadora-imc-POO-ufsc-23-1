import PySimpleGUI as sg
class CalculoIMC:
    def __init__(self):
        self.__peso = None
        self.__altura = None
    
    def buildWindow(self):
        linha0= [sg.Text("Qual seu peso"), sg.InputText("",key ="peso"), sg.Text("Kg")]
        linha1= [sg.Text("Qual sua altura"), sg.InputText("",key ="altura"), sg.Text("cm")]
        linha2= [sg.Text("Seu IMC é"), sg.InputText("",key ="imc", size=(6,1))]
        linha3= [sg.Text("",size=(14,1)), sg.Button("-CALCULAR IMC-")]
        container = [linha0,linha1,linha2,linha3]
        return container

    def calculateIMC(self,values):
       # alturaStr = values["altura"].replace(",","").replace(".","")
        self.__peso = float(values["peso"])
        self.__altura = float(values["altura"])/100
        imc = self.__peso/(self.__altura**2)
        return round(imc,2)

    def run(self):
        window = sg.Window("Calculadora de IMC", self.buildWindow(), font=("Helvetica", 14))

        rodando = True
        while rodando:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == '-CALCULAR IMC-':
                imc = self.calculateIMC(values)
                window.Element("imc").Update(imc)