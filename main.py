
def fibonacci(n):
    # Inicializa a sequência com os dois primeiros números
    seq = [0, 1]
    # Gera a sequência até o n-ésimo termo
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

# Programa principal
if __name__ == '__main__':
    # Solicita ao usuário um número inteiro positivo
    n = int(input("Informe um número inteiro positivo: "))
    if n <= 0:
        print("Por favor, informe um número inteiro positivo.")
    else:
        # Chama a função fibonacci e imprime a sequência
        resultado = fibonacci(n)
        print(f"A sequência de Fibonacci com {n} termos é: {resultado}")