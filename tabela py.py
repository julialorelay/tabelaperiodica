Sigla_elemento = input("Digite a sigla do elemento: ")

elementos = {
    "H": {"numero": 1, "massa": "1.00794", "nome": "hidrogenio"},
    "P": {"numero": 15, "massa": "30.973762", "nome": "fosforo"},
    "U": {"numero": 92, "massa": "238.02891", "nome": "uranio"}
}

if Sigla_elemento in elementos:
    elemento = elementos[Sigla_elemento]
    print(f"Elemento: {elemento['nome']}")
    print(f"Número atômico: {elemento['numero']}")
    print(f"Massa atômica: {elemento['massa']}")
else:
    print("Sigla não reconhecida. Por favor, corrija o programa.")