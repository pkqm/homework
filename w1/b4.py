c = input("Nhập vào một kí tự: ")
if len(c) == 1 and (('a' <= c <= 'z') or ('A' <= c <= 'Z')):
    print(f"{c} là kí tự alphabet")
else:
    print(f"{c} không phải là kí tự alphabet")