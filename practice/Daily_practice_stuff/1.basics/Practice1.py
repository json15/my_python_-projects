# 1. Change a normal number to binary number
def question_1(input_num):
    result = ''
    while input_num != 0:
        decimal = input_num % 2
        result = str(decimal) + result
        input_num = input_num // 2
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

    while user_input != 0:
        user_input = input('Please, enter number between 1,9(0 to exit): ')
        try:
            user_input = int(user_input)
        except:
            print('It is not a number, Pleace enter again')
            continue

        if 0< user_input <10:
            for i in range(1,10):
                result = i * user_input
                print('%s X %s = %s' %(user_input, i, result))
        elif user_input != 0:
            print('Wrong input, Please enter again.')
    print('Thank you for using this program')


# 3. get the mean value for each student
# 1. use zip(), 2. do not use zip
# subject scorse [50, 80, 90, 30, 70], [76, 39, 91, 88, 10], [95, 85, 33, 10, 100]
def question_3a(*args):
    avg_score = []
    for i in zip(*args):
        avg_score.append(sum(i) / len(args))

    for i,v in enumerate(avg_score):
        if i == 0:
            print('%dst students average score is %d' % (i+1, v))
        elif i == 1:
            print('%dnd students average score is %d' % (i+1, v))
        elif i == 2:
            print('%drd students average score is %d' % (i + 1, v))
        else:
            print('%dth students average score is %d' % (i+1, v))

    result = 0
    return result


def question_3b(*args):
    avg_score = []
    student_score = [0, 0, 0, 0, 0]

    for j in range(len(args[0])):
        for i in args:
            student_score[j] += i[j]

    for i in student_score:
        avg_score.append(i/3)

    print(avg_score)





if __name__ == '__main__':
    # print(question_1(10))
    # print(question_2(3))
    # print(question_3a([50, 80, 90, 30, 70], [76, 39, 91, 88, 10], [95, 85, 33, 10, 100]))
    print(question_3b([50, 80, 90, 30, 70], [76, 39, 91, 88, 10], [95, 85, 33, 10, 100]))