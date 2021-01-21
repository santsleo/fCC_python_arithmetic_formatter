def arithmetic_arranger(problems, result=False):

    l1, l2, l3, l4 = '', '', '', ''

    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_prob = True
    for prob in problems:

        parts = prob.split()

        # Validity checks
        if len(parts) > 3:
            return 'Error: only three inputs per part are allowed.'

        try:
            n1 = str(int(parts[0]))
            n2 = str(int(parts[2]))
        except:
            return 'Error: Numbers must only contain digits.'

        op = parts[1]

        if op == '+':
            sum = True
        elif op == '-':
            sum = False
        else:
            return "Error: Operator must be '+' or '-'."

        if len(str(n1)) > 4 or len(str(n2)) > 4:
            return "Error: Numbers cannot be more than four digits."

        res = str(int(n1) + int(n2)) if sum == True else str(int(n1) - int(n2))

        n1_spaces = len(n2) - len(n1) if len(n2) > len(n1) else 0
        n2_spaces = len(n1) - len(n2) if len(n1) > len(n2) else 0

        prob_sep = ' ' * 4

        if first_prob:
            l1 += ' ' * 2 + ' ' * n1_spaces + n1
            l2 += op + ' ' + ' ' * n2_spaces + n2

            prob_length = len(l1) if len(l1) > len(l2) else len(l2)

            l3 += '-' * prob_length
            l4 += ' ' * (prob_length - len(res)) + res

            first_prob = False
        else:
            current_l1 = ' ' * 2 + ' ' * n1_spaces + n1
            l1 += prob_sep + current_l1
            current_l2 = op + ' ' + ' ' * n2_spaces + n2
            l2 += prob_sep + current_l2

            prob_length = len(current_l1) if len(
                current_l1) > len(current_l2) else len(current_l2)

            l3 += prob_sep + '-' * prob_length
            l4 += prob_sep + ' ' * (prob_length - len(res)) + res

    if result:
        return l1 + '\n' + l2 + '\n' + l3 + '\n' + l4

    return l1 + '\n' + l2 + '\n' + l3
