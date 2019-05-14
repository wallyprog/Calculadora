# Uma calculadora para obter o valor de expressões aritméticas inteiras com parênteses.
# A interface gráfica é usada para montar a expressão a ser calculada.
# A tecla "=" chama o comando eval do Python para calcular a expressão.
# No caso de uma operação que resultar em erro, a exceção produz o resultado "erro"
# Adaptado do exemplo disponível em http://www.ufpel.tche.br/~campani/laminas.pdf
# Atenção: em Python, constantes precedidas por 0 são consideradas octais.
# Por esse motivo, 08, 008, 09, 085, etc são números inválidos.
# A calculadora deveria remover os zeros à esquerda de todos os números.
# Este programa faz isso parcialmente, apenas com o primeiro número.
# Cuidado deve ser tomado ao entrar com os outros valores.


from tkinter import *

# Criando os widgets:
e=""  # A string que aparece no display da calculadora, inicialmente vazia.
root = Tk()
root.title("Calculadora")
frame = Frame(root)
frame2 = Frame(root)
frame.pack(side=TOP)
frame2.pack(side=TOP)
lb = Label(frame,text="",width = 24,relief=RIDGE, font="Arial 12 bold",\
           fg="blue")
lb.pack(fill=Y)
b0 = Button(frame2,text="0",bd=3,padx=1,pady=1, width=8, height=2)
b1 = Button(frame2,text="1",bd=3,padx=1,pady=1, width=8, height=2)
b2 = Button(frame2,text="2",bd=3,padx=1,pady=1, width=8, height=2)
b3 = Button(frame2,text="3",bd=3,padx=1,pady=1, width=8, height=2)
b4 = Button(frame2,text="4",bd=3,padx=1,pady=1, width=8, height=2)
b5 = Button(frame2,text="5",bd=3,padx=1,pady=1, width=8, height=2)
b6 = Button(frame2,text="6",bd=3,padx=1,pady=1, width=8, height=2)
b7 = Button(frame2,text="7",bd=3,padx=1,pady=1, width=8, height=2)
b8 = Button(frame2,text="8",bd=3,padx=1,pady=1, width=8, height=2)
b9 = Button(frame2,text="9",bd=3,padx=1,pady=1, width=8, height=2)
bmais = Button(frame2,text="+",bd=3,padx=1,pady=1, width=8, height=2)
bmenos = Button(frame2,text="-",bd=3,padx=1,pady=1, width=8, height=2)
bvezes = Button(frame2,text="x",bd=3,padx=1,pady=1, width=8, height=2)
bdiv = Button(frame2,text="/",bd=3,padx=1,pady=1, width=8, height=2)
bigual = Button(frame2,text="=",bd=3,padx=1,pady=1, width=8, height=2)
babre = Button(frame2,text="(",bd=3,padx=1,pady=1, width=8, height=2)
bfecha = Button(frame2,text=")",bd=3,padx=1,pady=1, width=8, height=2)
bclear = Button(frame2,text="C",bd=3,padx=1,pady=1, width=8, height=2)
boff = Button(frame2,text="OFF",bd=3,padx=1,pady=1, width=16, height=2,\
              command=root.quit)

# Packing:
b7.grid(row=0,column=0)
b8.grid(row=0,column=1)
b9.grid(row=0,column=2)
bvezes.grid(row=0,column=3)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
bmais.grid(row=1,column=3)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)
bmenos.grid(row=2,column=3)
b0.grid(row=3,column=0)
babre.grid(row=3,column=1)
bfecha.grid(row=3,column=2)
bdiv.grid(row=3,column=3)
boff.grid(row=4, column=0, columnspan=2,sticky="NESW")
bclear.grid(row=4,column=2)
bigual.grid(row=4,column=3)


# Callbacks:
def digito(ev):
    global e,lb
    #remove os zeros à esquerda se o segundo caractere for dígito:
    if len(e) > 1 and e[1].isdigit():
        e = e.lstrip('0')
        lb.config(text=e)
    if ev.widget==b0:
        e+="0"
        lb.config(text=e)
    elif ev.widget==b1:
        e+="1"
        lb.config(text=e)        
    elif ev.widget==b2:
        e+="2"
        lb.config(text=e)
    elif ev.widget==b3:
        e+="3"
        lb.config(text=e)
    elif ev.widget==b4:
        e+="4"
        lb.config(text=e)
    elif ev.widget==b5:
        e+="5"
        lb.config(text=e)
    elif ev.widget==b6:
        e+="6"
        lb.config(text=e)
    elif ev.widget==b7:
        e+="7"
        lb.config(text=e)
    elif ev.widget==b8:
        e+="8"
        lb.config(text=e)
    else: 
        e+="9"
        lb.config(text=e)

def opera(ev):
    global e,lb
    if ev.widget==bmais:
        e += "+"
        lb.config(text=e)
    elif ev.widget==bmenos:
        e += "-"
        lb.config(text=e)
    elif ev.widget==bvezes:
        e += "*"
        lb.config(text=e)
    elif ev.widget==bdiv:
        e += "/"
        lb.config(text=e)

def parenteses(ev):
    global e,lb
    if ev.widget==babre:
        e += "("
        lb.config(text=e)
    elif ev.widget==bfecha:
        e += ")"
        lb.config(text=e)

# Tecla '=' acionada:
def finaliza(ev):
    global e,lb
    try:
        r = eval(e)  # a função eval lança exceção se não puder calcular
        e= str(r)
        lb.config(text= e)       
    except:
        lb.config(text="erro!")
        

def clear(ev):
    global e,lb
    e = "0"
    lb.config(text = e)
    


# Binding:
b0.bind("<Button-1>",digito)
b1.bind("<Button-1>",digito)
b2.bind("<Button-1>",digito)
b3.bind("<Button-1>",digito)
b4.bind("<Button-1>",digito)
b5.bind("<Button-1>",digito)
b6.bind("<Button-1>",digito)
b7.bind("<Button-1>",digito)
b8.bind("<Button-1>",digito)
b9.bind("<Button-1>",digito)
bmais.bind("<Button-1>",opera)
bmenos.bind("<Button-1>",opera)
bvezes.bind("<Button-1>",opera)
bdiv.bind("<Button-1>",opera)
babre.bind("<Button-1>",parenteses)
bfecha.bind("<Button-1>",parenteses)
bigual.bind("<Button-1>",finaliza)
bclear.bind("<Button-1>",clear)


#Mainloop:
root.mainloop()