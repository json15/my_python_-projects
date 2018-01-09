# 1. Change a normal number to binary number
def question_1(decimal):
    result = ''

    while decimal != 0:
        reminder = decimal % 2
        decimal = decimal // 2
        result = str(reminder) + result

    return result


# 2. Make a function that is capable of returning the value of
#Please, enter number between 1,9(0 to exit): 5
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45
# Please, enter number between 1,9(0 to exit): a
# Wrong input
# Please, enter number between 1,9(0 to exit): 0
# Thank you for using this program
def question_2(user_input):

    while True:
        user_input = input('Please, enter number between 1,9(0 to exit): ')

        try:
            user_input = int(user_input)
        except:
            print('Wrong input')
            continue

        if not 0 <= user_input <= 10:
            print('Wrong input')
        elif user_input == 0:
            print('Thank you for using this program')
            break
        else:
            for i in range(1, 10):
                answer = i * user_input
                print('{0} X {1} = {2}'.format(user_input, i, answer))


# 3. get the mean value for each student
# kor_score = [50, 80, 90, 30, 70]
# math_score = [76, 39, 91, 88, 10]
# eng_score = [95, 85, 33, 10, 100]
def question_3():
    kor_score = [50, 80, 90, 30, 70]
    math_score = [76, 39, 91, 88, 10]
    eng_score = [95, 85, 33, 10, 100]
    average_score = []

    for i in zip(kor_score, math_score, eng_score):
        score = sum(i) / 3
        average_score.append(score)

    print(average_score)

def question_3a():
    kor_score = [50, 80, 90, 30, 70]
    math_score = [76, 39, 91, 88, 10]
    eng_score = [95, 85, 33, 10, 100]
    average_score = [kor_score, math_score, eng_score]
    student_score = [0, 0, 0, 0, 0]
    result = []


    for subject in average_score:
        i = 0
        for score in subject:
            student_score[i] += score
            i += 1

    for i in student_score:
        result.append(i /3)

    print(result)









if __name__ == '__main__':
    # print(question_1(100))
    # print(question_2('a'))
    # print(question_3())
    print(question_3a())