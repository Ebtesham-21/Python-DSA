n = int(input("Enter a number: "))
def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n-1)