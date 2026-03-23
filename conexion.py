
import tkinter as tk
import subprocess
import os

root = tk.Tk()
root.title("Dashboard Charlx") #nombre de la pestaña
root.geometry("400x250")
#ese nos define las dimensiones del display
#leera el archivo
def abrir_dashboard():
    ruta = os.path.abspath("nuevo.py")#Convierte el name del archiv "nuevo.py" en una ruta completa del sistema
    #osea nuevo.py no se sabe su ubicacion pero con abspath ya lo lee como c\discolocal etc
    subprocess.Popen(["streamlit", "run", ruta]) #Ejecuta un programa externo desde Python.


titulo = tk.Label(root, text="sistema de dashboard charlx", font=("arial",16,"bold"),fg="blue")
#la letra del texto que estara dentro es blue
#el root indicamos en q ventana va, 
titulo.pack(pady=20) # indica la separacion de arriba y abajo
btn= tk.Button(root, text="ir a dashboard", command= abrir_dashboard, bg="gray", fg="white")
#crea un boton, el command hace que la funcion se ejecute al hacer click
btn.pack(expand=True, pady=20)
#expand hace q el boton use el espacio disponible, 


root.resizable(10,10) #esto evita que se pueda modificar la ventanta (extender)
root.mainloop() #esto hace un loop para que el programa no se cierre hasta interaccion


