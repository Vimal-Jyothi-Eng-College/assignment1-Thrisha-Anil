list = [10, 20, 30, 40, 50]
n = int(input("Enter index to delete: "))
if 0 <= n < len(list):
    del list[n]
else:
    print("Invalid index")
print(list)
