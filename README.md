# TallerHerramineta

## Punto 1
Este algoritmo recive 2 variables como entrada unhace referencia al largo de la base y otral a la altura, y tiene como salida la variable ares que es el producto de la multiplicacion de la base por la altura, sobre 2, la implimentacion fue echa en Python y puede verse en: **_Punto1.py_**

```python
s = "Python syntax highlighting"
def triangulo(a,b):

    area = (b * a)/2

    print(area)


triangulo(30,50)
```
## Punto 2
este algoritmo recive 4 variables tipo **int** referentes a 2 notas de parciales una nota de taller y la nota de un proyecto, y tiene como salida la nota final que ese calcula sacando los respectivos porsentajes a cada nota y sumandolos, es el 25% para cada uno de los parciales, el 30% proyecto final y el 20% al taller. La implementacion fue echa en Python y puede verse en: **_Punto2.py_**

```python
s = "Python syntax highlighting"
def nota(p1,p2,t,p):

    notafp1 = p1 * (25/100)
    notafp2 = p2 * (25/100)
    notat = t * (20/100)
    notafp = p * (30/100)

    notafinal = notafp1 + notafp2 + notat + notafp

    print(notafinal)

nota(5,3.5,5,4)
```
## Punto3
Este algoritmo recibe una varialbe (c) tipo **int** referente a un numero de grados celcious y tiene como salida (t) que es la conversion de grados celcious a Fahrenheit, que se hizo con la formula (c * (9/5))+32. La implementacion fue echa en Python y puede verse en el archivo:  **_Punto3.py_**

```python
s = "Python syntax highlighting"
def transformacion(c):

    t = (c * (9/5))+32

    print(t)


transformacion(100)
```
## Punto4
Este algoritmo pide como entrada la variable p que es un diccionario que guarda el nombre de varios productos como claves y a cada clave le asigna una  lista con una descripcion y el precio del respectivo producto, y tiene como salida el precio final de una compra realizada. La implementacion fue echa en Python y puede verse en el archivo:  **_Punto4.py_**
```python
s = "Python syntax highlighting"
p = {"gaseosa":["bedida de Gas", 5000],
     "pizza":["Pizza de champiñones y pollo",4000],
     "queso":["50 rodajas de queso de marca adidas", 3500],
     "jamon":["30 rodajas de jamon de marca nike", 4000],
     "pan":["pan bimbo recien horneado", 1000]}

def tiendita(p):

    quiere = True

    print("estos son los productos disponiles")
    
    for i in p:

        print(i)

    preciototal = 0

    while quiere == True:

        pagart = 0

        producto = str(input("Escriba su producto: "))

        pagart = pagart + (p[producto][1] + p[producto][1]*(8/100))

        preciototal += pagart

        print("el artículo comprado  es: ",p[producto][0], " y el valor a pagar es: ",pagart,"con una iva del 8%")

        SioNo = str(input("Desea comprar algo más?"))

        if SioNo == "Si" or SioNo == "si":

            quiere = True

        else:

            quiere = False

    print("el precio final a pagar es: ",preciototal)
    
tiendita(p))
```
## Punto5
El algoritmo tiene como estrada una variable tipo **float** que es referenta a una cantidad de dinero y se guarda en la varialbe dinero y tiene como salida su respectivo cambio a dolares, euros y yenes. La implementacion fue echa en Python y puede verse en el archivo:  **_Punto5.py_**
```python
s = "Python syntax highlighting"
def casacambio(dinero):

    dolares = (dinero/3652.50) + (dinero/3652.50)*2/100

    euros = (dinero/4422.64) + (dinero/4422.64)*2/100

    yenes = (dinero/33.16) + (dinero/33.16)*2/100

    print("Dolares: ", dolares, " Euros: ",euros," Yenes: ",yenes)

casacambio(100000)
```

## Punto6
El algoritmo tiene como entrada 30 variables tipo **float** que hacen referencia al promedio de notas de 30 estudiantes cada una se guanda en la variable n1, n2 ,n3 ...n30 y tiene como salida el promedio mayor de los 30 estudiantes. La implementacion fue echa en Python y puede verse en el archivo:  **_Punto6.py_**

```python
s = "Python syntax highlighting"
def inventario(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25,n26,n27,n28,n29,n30)
    estudiantes = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25,n26,n27,n28,n29,n30]
    print(max(estudiantes))


inventario(4.5,4.6,4.7,4.8,4.9,5.0,4.2,4.3,4.1,4.0,4.4,3.9,3.8,3.7,3.6,3.5,3.0,3.1,2.9,2.8,2.7,2.6,2.5,2.4,2.3,2.1,2.0,1.9,1.8,1.7)

```
