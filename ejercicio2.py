def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 5
#perro
print("El factorial de", num, "es", factorial(num))