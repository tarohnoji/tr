i = 1

while i < 5:
    num = input("数字を入力してください：")
    num = int(num)

    if num % 2 == 0:
        print("偶数ですね")

    elif num % 2 == 1:
        print("奇数ですね")

    i += 1

