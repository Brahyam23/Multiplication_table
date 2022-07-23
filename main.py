#Funcion tabla de multiplicar
def tabla_multiplicar(num):
    
    with open("Tabla del "+ str(num)+".txt", "a") as f:

        for i in range(11):
            m=num*i
            f.write(f"{num} x {i} = {m}\n")


tabla_multiplicar(5)