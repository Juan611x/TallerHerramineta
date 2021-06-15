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
    
tiendita(p) 
