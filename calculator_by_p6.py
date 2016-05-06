##############Simple Calculator#################
##############brought to you by#################
################### P6[B] #########################

import operator

# 1.question variables
first_number = 'Enter a number (or a letter to exit): '
second_number = 'Enter another number: '
operator_question = 'Enter an operation: '

# 2. operator module dictionary
operators = {"+": operator.add,
             "-": operator.sub,
             "*": operator.mul,
             "/": operator.truediv}

# 3.functions

# 3.1 change int() to float() to make it work with float numbers too
def number_ask(question):
    try:
        answer = int(input(question))
    except ValueError:
        exit()
    return int(answer)


def operator_ask(question,available_answers):
    answer = input(question)
    if answer not in available_answers:
        return operator_ask(question,available_answers)
    return answer


def calculate_it(num1,num2,operand,dictionary):
    function = dictionary[operand]
    result = function(num1,num2)
    print ("Result: %s " %(result))
    return ''



# bring it on!
def endless_story():
    number_one = (number_ask(first_number))
    operand = (operator_ask(operator_question,operators))
    number_two = (number_ask(second_number))
    print(calculate_it(number_one,number_two,operand,operators))
    return endless_story()

print (endless_story())
