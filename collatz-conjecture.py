x = input("Enter a number: ")
count = 0
x = int(x)
while True:
    count = count + 1
    if x % 2 != 0:
        x = x * 3 + 1
    else:
        x = x // 2
    print(f"{x:,}  ", end='')
    if x == 1:
        print(f"\nIt took {count} steps to reach 1.")
        break