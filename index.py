import myDef

answer_count = 1
print("Great&Goodを開始します！")
answer_number_ary = myDef.make_random_number()
maped_num = map(str, answer_number_ary)
answer_number = ''.join(maped_num)


great_count = 0
good_count = 0


print(str(answer_count) + "回目のチャレンジ！")
(my_answer_number, my_answer_number_ary) = myDef.input_and_check()
while answer_count < 10:
    answer_count += 1
    for i in range(3):
        for j in range(3):
            if i == j and answer_number_ary[i] == my_answer_number_ary[j]:
                great_count += 1
            elif i != j and answer_number_ary[i] == my_answer_number_ary[j]:
                good_count += 1
    if great_count == 3:
        print("正解です！")
        break
    else:
        print("Great:" + str(great_count))
        print("Good:" + str(good_count))
        print("")
        great_count = 0
        good_count = 0
        print(str(answer_count) + "回目のチャレンジ！")
        (my_answer_number, my_answer_number_ary) = myDef.input_and_check()
else:
    for i in range(3):
        for j in range(3):
            if i == j and answer_number_ary[i] == my_answer_number_ary[j]:
                great_count += 1
            elif i != j and answer_number_ary[i] == my_answer_number_ary[j]:
                good_count += 1
    if great_count == 3:
        print("正解です！")
    else:
        print("Great:" + str(great_count))
        print("Good:" + str(good_count))
        print("")
        print("残念でした。答えは" + answer_number + "です。")
    
