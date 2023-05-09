import PySimpleGUI as sg

class IMCCalculator:
    def __init__(self):
        self.__layout = [sg.Text("Qual seu peso"), sg.InputText("",key ="peso"), sg.Text("Kg"),
                         sg.Text("Qual sua altura"), sg.InputText("",key ="altura"), sg.Text("cm"),
                         sg.Text("Seu IMC é"), sg.InputText("",key ="imc", size=(6,1)),
                         sg.Text("",size=(14,1)), sg.Button("CALCULAR IMC")]
        self.__height = None
        self.__weight = None
    
    def calculateIMC(self,values):
        heightStr = values["height"].replace(",","").replace(".","")
        self.__weight = float(values["weight"])
        self.__height = float(heightStr)/100
        imc = self.__weight/(self.__height**2)
        return round(imc,2)
    