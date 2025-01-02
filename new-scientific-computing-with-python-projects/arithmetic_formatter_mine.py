#########################################
# Build an Arithmetic Formatter Project #
#########################################
"""
Finish the arithmetic_arranger function that receives a list of strings which are
arithmetic problems, and returns the problems arranged vertically and side-by-side.
The function should optionally take a second argument. When the second argument is
set to True, the answers should be displayed.

Rules
    The function will return the correct conversion if the supplied problems are properly formatted,
    otherwise, it will return a string that describes an error that is meaningful to the user.

    Situations that will return an error:
        # If there are too many problems supplied to the function.
            The limit is five, anything more will return: 'Error: Too many problems.'
        # The appropriate operators the function will accept are addition and subtraction.
            Multiplication and division will return an error. Other operators not mentioned
            in this bullet point will not need to be tested. The error returned will be:
            "Error: Operator must be '+' or '-'."
        # Each number (operand) should only contain digits. Otherwise, the function will return:
            'Error: Numbers must only contain digits.'
        # Each operand (aka number on each side of the operator) has a max of four digits in width.
            Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'

    If the user supplied the correct format of problems, the conversion you return will follow these rules:
        # There should be a single space between the operator and the longest of the two operands,
            the operator will be on the same line as the second operand, both operands will be in the same
            order as provided (the first will be the top one and the second will be the bottom).
        # Numbers should be right-aligned.
        # There should be four spaces between each problem.
        # There should be dashes at the bottom of each problem. The dashes should run along the entire length
            of each problem individually. (The example above shows what this should look like.)

Example 1:
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----

Example 2:
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
"""

MAX_NUM_QUESTION = 5
MAX_OPERAND_LENGTH = 4
N_CHARS_BTW_PROBLEM = 4

BAR_CHAR = '-'
PROBLEM_SEPARATOR = ' '

VALID_OPERATORS = ['+', '-', '*', '/', '%']

INVALID_QUESTION_LIMIT_ERROR_MSG = 'Error: Too many problems.'
INVALID_OPERATOR_ERROR_MSG = f"Error: Operator must be one of {VALID_OPERATORS}."
INVALID_OPERAND_VALUE_ERROR_MSG = 'Error: Numbers must only contain digits.'
INVALID_OPERAND_LENGTH_ERROR_MSG = f'Error: Numbers cannot be more than {MAX_OPERAND_LENGTH} digits.'


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
        # print(problems_table)
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
                           + PROBLEM_SEPARATOR * N_CHARS_BTW_PROBLEM)

    for prob in problems_dict:
        line_operand_2 += (prob['operator'] + ' '+ prob['second_operand'].rjust(prob['max_operand_length'])
                           + PROBLEM_SEPARATOR * N_CHARS_BTW_PROBLEM)

    for prob in problems_dict:
        line_separator += (BAR_CHAR * (prob['max_operand_length'] + 2)
                           + PROBLEM_SEPARATOR * N_CHARS_BTW_PROBLEM)

    if show_answer:
        line_answer += '\n'
        for prob in problems_dict:
            line_answer += (str(prob['answer']).rjust(prob['max_operand_length'] + 2)
                            + PROBLEM_SEPARATOR * N_CHARS_BTW_PROBLEM)

    display_table = (line_operand_1.rstrip() + '\n' + line_operand_2.rstrip() + '\n'
                     + line_separator.rstrip() + line_answer.rstrip())
    return display_table


def compute_problems(problems_dict):
    """
    Compute the correct answer to each problem.
    And update the max_operand_length values

    :param problems_dict: a list of validated problems each in a dictionary.
    :return: a list of validated problems with answer each in a dictionary.
    """
    for prob in problems_dict:
        first_operand = int(prob['first_operand'])
        second_operand = int(prob['second_operand'])

        if prob['operator'] == '+':
            prob['answer'] = first_operand + second_operand
        elif prob['operator'] == '-':
            prob['answer'] = first_operand - second_operand
        elif prob['operator'] == '*':
            prob['answer'] = first_operand * second_operand
        elif prob['operator'] == '/':
            prob['answer'] = int(first_operand / second_operand)
        else:
            prob['answer'] = first_operand % second_operand

        prob['max_operand_length'] = max(prob['max_operand_length'], len(str(prob['answer'])))

    return problems_dict


def validate_problems(problems_list):
    """
    Checks if each problem is in the required format.

    :param problems_list: a list of problems.
    :return: a list of validated problems each in a dictionary.
    """

    is_error = True

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


table = arithmetic_arranger(["3801 - 2", "123 + 49", "2300 * 1000", "512 / 32", "512 % 32"], True)
print(table)