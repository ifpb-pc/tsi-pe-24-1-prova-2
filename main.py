def q1(cidades):
    return [cidade for cidade, idade in cidades.items() if idade > 100] 

def q2(lista1, lista2):
    positivos = [x for x in lista1 + lista2 if x > 0]
    
    soma = sum(positivos)
    
    positivos_ordenados = sorted(positivos)
    
    return soma, positivos_ordenados 

def q3():
    valores = []
    while True:
        n = int(input("Digite um número (e 0 para parar)"))
        if n == 0:
            break 
        valores.append(n)
        

        
    pares = [ x for x in valores if x % 2 == 0]
    impares = [x for x in valores if x % 2 != 0]

    print("lista de pares:", pares)
    print("Lista de ímpares:", impares) 
    return pares, impares

def ler_03_alturas():
    alturas = []
    for i in range(3):
        h = float(input(f"Digite a altura da pessoa {i+1}: "))
        alturas.append(h)
    return alturas

def organizar_alturas(alturas):
    alturas_ordenadas = sorted(alturas)
    return [alturas_ordenadas[1], alturas_ordenadas[2], alturas_ordenadas[0]]

def formatar_alturas(alturas):
    return [f"{h:.2f}" for h in alturas]

def q4():
    alturas = ler_03_alturas()
    organizadas = organizar_alturas(alturas)
    formatadas = formatar_alturas(organizadas)
    for altura in formatadas:
        print(altura)




def main():
    # Teste as questões que você desenvolveu manualmente:
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    resultado = q1(idades)
    print("q1:", resultado)


    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    resultado = q2(lista1, lista2)
    print("q2:", resultado)


 



if __name__ == "__main__":
    main()


