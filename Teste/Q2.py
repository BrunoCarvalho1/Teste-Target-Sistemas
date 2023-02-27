def teste1(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num:
        return f"{num} pertence à sequência de Fibonacci"
    else:
        return f"{num} não pertence à sequência de Fibonacci"
    
# Exemplo de uso
print(teste1(8))  # 8 pertence à sequência de Fibonacci
print(teste1(10)) # 10 não pertence à sequência de Fibonacci