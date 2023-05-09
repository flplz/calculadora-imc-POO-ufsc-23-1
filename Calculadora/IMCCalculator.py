import PySimpleGUI as sg

class IMCCalculator:
    def __init__(self):
        self.__running = True
        self.__window = None
        self.__title = "IMC Calculator"

    def buildWindow(self):
        linha0= [sg.Text("Qual seu peso"), sg.InputText("",key ="weight"), sg.Text("Kg")]
        linha1= [sg.Text("Qual sua altura"), sg.InputText("",key ="height"), sg.Text("cm")]
        linha2= [sg.Text("Seu IMC é"), sg.InputText("",key ="imc", size=(6,1))]
        linha3= [sg.Text("",size=(14,1)), sg.Button("CALCULAR IMC")]
        container = [linha0,linha1,linha2,linha3]
        return container
        
    def calculateIMC(self,values):
        heightStr = values["height"].replace(",","").replace(".","")
        weight = float(values["weight"])
        height = float(heightStr)/100
        imc = weight/(height**2)
        return round(imc,2)
    
    
    def loop(self):
        self.__window = sg.Window(self.__title, self.buildWindow(), font=("Helvetica", 14))
        
        try:
            while self.__running:
                event, values = self.__window.read()
                
                if event == sg.WIN_CLOSED:
                    self.__running = False
                elif event == "CALCULAR IMC":
                    imc = self.calculateIMC(values)
                    self.__window.Element("imc").Update(imc)
        except ValueError:
            sg.popup("Os valores de peso e altura devem ser números.")
        except ZeroDivisionError:
            sg.popup("A altura deve ser maior que zero.")
        except Exception as e:
            sg.popup(f"Ocorreu um erro: {e}")
        finally:
            self.__window.close()
    
    