print("#" * 21)
print("{}TABUADA{}".format(("#" * 7), ("#" * 7)))
print("#" * 21)
valor = int(input("Informe um número para saber sua tabuada: "))
print("{}".format("#" * 21))
print("Tabuada de {}".format(valor))
print("#" * 21)
var = 1
multi = 0
while var <= 10:
    print("{} X {} = {}".format((var), (valor), (valor * var)))
    var += 1
