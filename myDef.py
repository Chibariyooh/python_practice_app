import random

def make_random_number():
    ary = []
    while len(ary) < 3:
        random_number = random.randint(0, 9)
        append_flg = True

        for ary_element in ary:
            if ary_element == random_number:
                append_flg = False
                break
        if append_flg == True:
            ary.append(random_number)
        append_flg = True
    return ary



def input_and_check():
    input_number = input("3桁の数値を入力してください：")
    while True:
        input_number_ary = []
        if input_number.isdigit() == True and input_number.encode('utf-8').isalnum() == True and len(input_number) == 3:
            devision_number = int(input_number)
            for i in range(3):
                input_number_ary.append(devision_number // (10 ** (2-i)))
                devision_number = devision_number % (10 ** (2-i))
            if len(list(set(input_number_ary))) == 3:
                break
        input_number = input("【エラー】重複のない3桁の数値を入力してください：")
    return (input_number, input_number_ary)
