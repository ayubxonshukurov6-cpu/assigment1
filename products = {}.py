products = {}

for i in range(3):
    nom = input("Mahsulot nomi: ")
    narx = int(input("Narxi: "))
    products[nom] = narx

for nom, narx in products.items():
    if narx > 100000:
        narx = narx * 0.9
    print(nom, " ", narx)