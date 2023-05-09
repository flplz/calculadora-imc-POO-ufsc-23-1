import PySimpleGUI as sg

class IMCCalculator:
    def __init__(self):
        self.__running = True
        self.__window = None
        self.__title = "IMC Calculator"
        self.__imc_table = {
            (0, 18.4): "Abaixo do peso",
            (18.5, 24.9): "Peso normal",
            (25, 29.9): "Sobrepeso",
            (30, 34.9): "Obesidade grau 1",
            (35, 39.9): "Obesidade grau 2",
            (40, float("inf")): "Obesidade grau 3",
        }

    def buildWindow(self):
        rows = [
            [sg.Text("Qual seu peso"), sg.InputText("", key="weight"), sg.Text("Kg")],
            [sg.Text("Qual sua altura"), sg.InputText("", key="height"), sg.Text("cm")],
            [sg.Text("Seu IMC é"), sg.InputText("", key="imc", size=(6, 1))],
            [sg.Text("", size=(14, 1)), sg.Button("CALCULAR IMC")]
        ]
        return rows

    def calculateIMC(self,values):
        heightStr = values["height"].replace(",","").replace(".","")
        weight = float(values["weight"])
        height = float(heightStr)/100
        imc = weight/(height**2)
        result = "Desconhecido"
        for key in self.__imc_table:
            if key[0] <= imc <= key[1]:
                result = self.__imc_table[key]
                break
        return round(imc,2), result
    
    def loop(self):
        layout = [
            [sg.Column(self.buildWindow(), element_justification="center")]
        ]
        self.__window = sg.Window(self.__title, layout, font=("Helvetica", 14))
        while self.__running:
            event, values = self.__window.read()
            try:
                if event == sg.WIN_CLOSED:
                    self.__running = False
                elif event == "CALCULAR IMC":
                    imc, result = self.calculateIMC(values)
                    self.__window.Element("imc").Update(imc)
                    sg.popup(f"Seu IMC é {imc:.2f} ({result})")
            except ValueError:
                sg.popup("Os valores de peso e altura devem ser números.")
            except ZeroDivisionError:
                sg.popup("A altura deve ser maior que zero.")
            except Exception as e:
                sg.popup(f"Ocorreu um erro: {e}")
        self.__window.close()
    
    