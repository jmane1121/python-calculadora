# Importamos las librerías necesarias
import tkinter as tk
import math

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

# Creamos una variable para almacenar la operación
operacion = ""

# Creamos una función para capturar los números y operadores
def btnClick(num):
    global operacion
    operacion = operacion + str(num)
    input_text.set(operacion)

# Creamos una función para evaluar la operación y mostrar el resultado
def btnIgual():
    global operacion
    try:
        resultado = str(eval(operacion))
    except:
        resultado = "Error"
    input_text.set(resultado)

# Creamos una función para borrar la operación
def btnBorrar():
    global operacion
    operacion = ""
    input_text.set(operacion)

# Creamos una variable para mostrar el texto en la pantalla
input_text = tk.StringVar()

# Creamos la pantalla de la calculadora
pantalla = tk.Entry(ventana, font=("Arial", 20), textvariable=input_text, width=14, bd=5, justify="right")
pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Creamos los botones de la calculadora
btn1 = tk.Button(ventana, text="1", font=("Arial", 15), width=5, height=2, command=lambda: btnClick(1))
btn2 = tk.Button(ventana, text="2", font=("Arial", 15), width=5, height=2, command=lambda: btnClick(2))
btn3 = tk.Button(ventana, text="3", font=("Arial", 15), width=5, height=2, command=lambda: btnClick(3))
btn4 = tk.Button(ventana, text="4", font=("Arial", 15), width=5, height=2, command=lambda: btnClick(4))
btn5 = tk.Button(ventana, text="5", font=("Arial", 15), width=5, height=2, command=lambda: btnClick(5))
btn6 = tk.Button(ventana, text="6", font=("Arial", 15), width=5, height=2, command=lambda: btnClick(6))
btn7 = tk.Button(ventana, text="7", font=("Arial", 15), width=5, height=2, command=lambda: btnClick(7))
btn8 = tk.Button(ventana, text="8", font=("Arial", 15), width=5, height=2, command=lambda: btnClick(8))
btn9 = tk.Button(ventana, text="9", font=("Arial", 15), width=5, height=2, command=lambda: btnClick(9))
btn0 = tk.Button(ventana, text="0", font=("Arial", 15), width=11, height=2, command=lambda: btnClick(0))
btnPunto = tk.Button(ventana, text=".", font=("Arial", 15), width=5, height=2, command=lambda: btnClick("."))
btnSuma = tk.Button(ventana, text="+", font=("Arial", 15), width=5, height=2, bg="orange", command=lambda: btnClick("+"))
btnResta = tk.Button(ventana, text="-", font=("Arial", 15), width=5, height=2, bg="orange", command=lambda: btnClick("-"))
btnMulti = tk.Button(ventana, text="*", font=("Arial", 15), width=5, height=2, bg="orange", command=lambda: btnClick("*"))
btnDivi = tk.Button(ventana, text="/", font=("Arial", 15), width=5, height=2, bg="orange", command=lambda: btnClick("/"))
btnIgual2 = tk.Button(ventana, text="=", font=("Arial", 15), width=5, height=2, bg="green", command=lambda: btnIgual())
btnBorrar2 = tk.Button(ventana, text="C", font=("Arial", 15), padx=20, width=19, height=2, bg="red", command=lambda: btnBorrar())

# Colocamos los botones en la ventana
btn7.grid(row=1, column=0, padx=(10), pady=(10))
btn8.grid(row=1, column=1, padx=(10), pady=(10))
btn9.grid(row=1, column=2, padx=(10), pady=(10))
btnDivi.grid(row=1, column=3, padx=(10), pady=(10))

btn4.grid(row=2, column=0, padx=(10), pady=(10))
btn5.grid(row=2, column=1, padx=(10), pady=(10))
btn6.grid(row=2, column=2, padx=(10), pady=(10))
btnMulti.grid(row=2, column=3, padx=(10), pady=(10))

btn1.grid(row=3, column=0, padx=(10), pady=(10))
btn2.grid(row=3, column=1, padx=(10), pady=(10))
btn3.grid(row=3, column=2, padx=(10), pady=(10))
btnResta.grid(row=3, column=3, padx=(10), pady=(10))

btn0.grid(row=4, columnspan=2, padx=(10), pady=(10))
btnPunto.grid(row=4, column=2, padx=(10), pady=(10))
btnSuma.grid(row=4, column=3, padx=(10), pady=(10))

btnBorrar2.grid(row=5, columnspan=3, padx=(10), pady=(10))
btnIgual2.grid(rowspan=2, row=5, column=3, padx=(10), pady=(10))

# Iniciamos el bucle principal de la ventana
ventana.mainloop()

