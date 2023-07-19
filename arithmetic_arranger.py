# This code was made by NIDHAL LABRI #
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    line1 = line2 = line3 = line4 = ""

    for problem in problems:
        num1, operator, num2 = problem.split()
        #Errors check
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2
        line1 += num1.rjust(width) + "    "
        line2 += operator + " " + num2.rjust(width - 2) + "    "
        line3 += "-" * width + "    "

        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            line4 += answer.rjust(width) + "    "

    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
  
    if show_answers:
        arranged_problems += "\n" + line4.rstrip()

    return arranged_problems