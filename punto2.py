def nota():


    p1 = float(input())
    p2 = float(input())
    t = float(input())
    p = float(input())

    notafp1 = p1 * (25/100)
    notafp2 = p2 * (25/100)
    notat = t * (20/100)
    notafp = p * (30/100)

    notafinal = notafp1 + notafp2 + notat + notafp

    print(notafinal)

nota()
