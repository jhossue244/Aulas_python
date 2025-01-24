listagem = ("Lápis", 1.50,
            "borracha", 2,
            "Caderno", 19.99,
            "Estojo", 13.49,
            "Tranferidor", 4.99,
            "Compasso", 10.99,
            "Mochila", 149.99,
            "Cantenas", 15.99,
            "livros", 34.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end = "")
    else:
        print(f"R${listagem[pos]:>7.2f}")