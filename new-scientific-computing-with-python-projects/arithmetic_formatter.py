MAX_NUM_QUESTION = 5
MAX_OPERAND_LENGTH = 4
N_SPACE_BTW_PROBLEM = 4

SPACE = ' '
VALID_OPERATORS = ['+', '-']

INVALID_QUESTION_LIMIT_ERROR_MSG = 'Error: Too many problems.'
INVALID_OPERATOR_ERROR_MSG = "Error: Operator must be '+' or '-'."
INVALID_OPERAND_VALUE_ERROR_MSG = 'Error: Numbers must only contain digits.'
INVALID_OPERAND_LENGTH_ERROR_MSG = 'Error: Numbers cannot be more than four digits.'


def arithmetic_arranger(problems_list, show_answer=False):
    """
    Computes and arrange problems into a table of specific format

    :param problems_list: a list of problems.
    :param show_answer: whether to display answer or not.
    :return: formatted table display of problems.
    """
    is_error, validation_value = validate_problems(problems_list)

    if is_error:
        print(validation_value)
        return validation_value

    else:
        problems_dict = validation_value
        compute_problems(problems_dict)
        problems_table = display_problems(problems_dict, show_answer)
        return problems_table


def display_problems(problems_dict, show_answer):
    """
    Arranges the problems into a table of required format.

    :param problems_dict: a list of validated problems with answer each in a dictionary.
    :param show_answer: whether to display answer or not.
    :return: table of problems in required format.
    """
    line_operand_1 = ''
    line_operand_2 = ''
    line_separator = ''
    line_answer = ''

    for prob in problems_dict:
        line_operand_1 += (prob['first_operand'].rjust(prob['max_operand_length'] + 2)
                           + SPACE*N_SPACE_BTW_PROBLEM)

    for prob in problems_dict:
        line_operand_2 += (prob['operator'] + SPACE + prob['second_operand'].rjust(prob['max_operand_length'])
                           + SPACE*N_SPACE_BTW_PROBLEM)

    for prob in problems_dict:
        line_separator += '-' * (prob['max_operand_length'] + 2) + SPACE*N_SPACE_BTW_PROBLEM

    if show_answer:
        line_answer += '\n'
        for prob in problems_dict:
            line_answer += str(prob['answer']).rjust(prob['max_operand_length'] + 2) + SPACE*N_SPACE_BTW_PROBLEM

    table = line_operand_1.rstrip() + '\n' + line_operand_2.rstrip() + '\n' + line_separator.rstrip() + line_answer.rstrip()
    return table


def compute_problems(problems_dict):
    """
    Compute the correct answer to each problem.

    :param problems_dict: a list of validated problems each in a dictionary.
    :return: a list of validated problems with answer each in a dictionary.
    """
    for prob in problems_dict:
        first_operand = int(prob['first_operand'])
        second_operand = int(prob['second_operand'])

        if prob['operator'] == '+':
            prob['answer'] = first_operand + second_operand
        else:
            prob['answer'] = first_operand - second_operand

    return problems_dict


def validate_problems(problems_list):
    """
    Checks if each problem is in the required format.

    :param problems_list: a list of problems.
    :return: a list of validated problems each in a dictionary.
    """

    is_error = True
    problems_dict = []

    # Checks if number of problems does not exceed the requirement.
    if len(problems_list) > MAX_NUM_QUESTION:
        return is_error, INVALID_QUESTION_LIMIT_ERROR_MSG

    # Converts each problem into a list of its own
    # gives a list in a list format [[prob_1], [prob_2], [prob_3], ...]
    problems_list = [q.split(" ") for q in problems_list]

    # Converts each problem into a dictionary
    # gives a dict in a list format [{prob_1}, {prob_2}, {prob_3}, ...]
    problems_dict = list(map(lambda question: {
        'first_operand': question[0],
        'operator': question[1],
        'second_operand': question[2],
        'answer': None,
        'max_operand_length': max(len(question[0]), len(question[1]), len(question[2]))
    }, problems_list))

    for prob in problems_dict:
        # Checks if operator is valid ('+' or '-').
        if prob['operator'] not in VALID_OPERATORS:
            return is_error, INVALID_OPERATOR_ERROR_MSG

        # Checks if maximum length of operands does not exist the required (MAX_OPERAND_LENGTH)
        if prob['max_operand_length'] > MAX_OPERAND_LENGTH:
            return is_error, INVALID_OPERAND_LENGTH_ERROR_MSG

        # Checks if operands contains only digits
        if (not prob['first_operand'].isdigit()) | (not prob['second_operand'].isdigit()):
            return is_error, INVALID_OPERAND_VALUE_ERROR_MSG

    is_error = False
    return is_error, problems_dict



my_answer = arithmetic_arranger(["3801 - 2", "123 + 49"])
fcc_answer = '  3801      123\n-    2    +  49\n------    -----'


print(len(fcc_answer), len(my_answer))
print(fcc_answer == my_answer)