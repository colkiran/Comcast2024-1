def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

iter = int(input("Enter the number of fibanocci series to be generated :"))
print("Fibanocci Series :")
for i in range(iter):
    print(fibonacci(i), end=" ")

