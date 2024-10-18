from customtkinter import CTk, CTkButton, set_appearance_mode, CTkTextbox
from asteval import Interpreter
import pyttsx3

aeval = Interpreter()

modo_dark = False
modo_acessibilidade= False
engine = pyttsx3.init()

#FUNÇÃO PARA MUDAR O TEMA
def mudar_tema():
    global modo_dark
    modo_dark= not modo_dark

    if modo_dark:
        set_appearance_mode("dark")
        botao_tema.configure(text="Modo Claro")
    else :
        set_appearance_mode("light")
        botao_tema.configure(text="Modo Escuro")

def alternar_acessibilidade():
    global modo_acessibilidade
   
    modo_acessibilidade = not modo_acessibilidade
   
    if modo_acessibilidade:
        voz("Modo de acessibilidade ativado.")

    else:
        voz("Modo de acessibilidade desativado.")

def calcular():
    calculo = texto_box.get("0.0", "end").strip()
    try:
        resultado = aeval(calculo)
        texto_box.delete('0.0', 'end')
        texto_box.insert('0.0', str(resultado))
        if modo_acessibilidade:  # Falar o resultado se o modo de acessibilidade estiver ativado
            voz(f"O resultado é {resultado}")
    except Exception as e:
        texto_box.delete('0.0', 'end')
        texto_box.insert('0.0', 'Erro')
        if modo_acessibilidade:  # Falar erro se o modo de acessibilidade estiver ativado
            voz("Erro ao calcular.")


def voz(texto):
    engine.say(texto)
    engine.runAndWait()



#JANELA DO APLICATIVO
app=CTk()
app.geometry("600x350")
app.title("Calculadora")

# Função para falar o número ao clicar

def clique_botao(valor):
    texto_box.insert("end", valor)
    if modo_acessibilidade:  # Falar o valor apenas se o modo de acessibilidade estiver ativado
        voz(valor)

#Botoes
btn7 = CTkButton(app,text='7', command= lambda:clique_botao(7), corner_radius=20, width=80, height=55, font=("arial", 30))
btn7.grid(row=2, column=5, padx=2, pady=2)

btn8 = CTkButton(app,text="8", command= lambda:clique_botao(8), corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn8.grid(row = 2, column= 6, padx= 2, pady = 2)

btn9= CTkButton(app,text="9", command= lambda: clique_botao(9), corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn9.grid(row = 2, column= 7, padx= 2, pady = 2)

btn4 = CTkButton(app,text="4", command= lambda: clique_botao(4), corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn4.grid(row = 3, column= 5, padx= 2, pady = 2)

btn5 = CTkButton(app,text="5", command= lambda: clique_botao(5), corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn5.grid(row = 3, column= 6, padx= 2, pady = 2)

btn6 = CTkButton(app,text="6", command= lambda: clique_botao(6), corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn6.grid(row = 3, column= 7, padx= 2, pady = 2)

btn1 = CTkButton(app,text="1", command= lambda: clique_botao(1), corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn1.grid(row = 4, column= 5, padx= 2, pady = 2)

btn2 = CTkButton(app,text="2", command= lambda: clique_botao(2), corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn2.grid(row = 4, column= 6, padx= 2, pady = 2)

btn3 = CTkButton(app,text="3", command= lambda: clique_botao(3), corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn3.grid(row = 4, column= 7, padx= 2, pady = 2)

btn0 = CTkButton(app,text="0", command= lambda: clique_botao(0), corner_radius= 20, width= 100, height = 55, font =("arial", 30))
btn0.grid(row = 5, column= 5, padx= 2, pady = 2)

btn_frac=CTkButton(app, text= ".", command= lambda :clique_botao("."), corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn_frac.grid(row = 5, column = 9, padx = 2, pady = 2)

btn_calcular= CTkButton(app, text="=", command = calcular, corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn_calcular.grid(row = 5, column = 6, padx = 2, pady = 2)

btn_limpar = CTkButton(app, text= "C", command= lambda : texto_box.delete("0.0","end"), corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn_limpar.grid(row = 5, column = 7, padx = 2, pady = 2)

btn_somar =CTkButton(app, text= "+", command= lambda : clique_botao("+"), corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn_somar.grid(row = 2, column = 8, padx = 2, pady = 2)

btn_subtrair=CTkButton(app, text= "-", command= lambda : clique_botao("-"), corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn_subtrair.grid(row = 3, column = 8, padx = 2, pady = 2)

btn_dividir=CTkButton(app, text= "/", command= lambda :clique_botao("/"), corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn_dividir.grid(row = 4, column = 8, padx = 2, pady = 2)

btn_multiplicar=CTkButton(app, text= "x", command= lambda : clique_botao("*"), corner_radius= 20, width= 80, height = 55, font =("arial", 30))
btn_multiplicar.grid(row = 5, column = 8, padx = 2, pady = 2)

#ICONE DO CABEÇALHO
app.iconbitmap(r"icon\icon_header.ico")
app.resizable(width=False, height=False)

#CAIXA DE TEXTO
texto_box = CTkTextbox(app, width= 480, height=70, corner_radius=10, border_width=5, border_color='#042940', font=(('Arial', 50))) 
texto_box.grid(row=1, column=5, columnspan=5, padx=5, pady=5)

def pressionar_tecla(event):
    tecla = event.char
    if tecla.isdigit() or tecla in ['+', '-', '*', '/', '.']:
        clique_botao(tecla)
    elif tecla == '\r':  # Enter key
        calcular()
    elif tecla.lower() == 'c':  # 'C' key to clear
        texto_box.delete("0.0", "end")

# Bind das teclas
app.bind("<Key>", pressionar_tecla)

#BOTÃO PARA A TROCA DE TEMA
botao_tema = CTkButton(master=app, text="Modo Escuro", font=("Arial", 13), command=mudar_tema, width= 110)
botao_tema.grid(row=4 , column=1, padx = 2, pady= 2)

#BOTÃO ACESSIBILIDADE
botao_acessibilidade = CTkButton(master=app, text="Acessibilidade", font=("Arial", 13), command=alternar_acessibilidade, width=110)
botao_acessibilidade.grid(row=5, column=1, padx=2, pady=2)

app.mainloop()