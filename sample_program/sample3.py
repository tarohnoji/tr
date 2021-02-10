def calc_plus(a, b):
    a = int(a)
    b = int(b)
    return a + b

print("足し算を実行します：")
a = input("数を入力：")
b = input("数を入力：")

print("結果は{}です".format(str(calc_plus(a, b)))) 
