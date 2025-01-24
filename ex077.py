palavras = ("aprender",
            "Programar",
            "linguagem",
            "Python",
            "Curso",
            "Gratis",
            "estudar",
            "Praticar",
            "Trabalhar",
            "Mercado",
            "Programador",
            "Futuro")

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos ", end = "")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end = "")
