
def num_first_extrct(exp):
    """
    5
    4

    """
    n = 0
    for c in exp:
        if c in ("*", "/", "+", "-"):
            break
        n = 10 * n + int(c)
    return n
    #print(f"Your first number is {n}")


# n1 = num_first_extrct("1235678-16+18")
# print(n1)
def op_first_extrct(exp):
    o = "o"
    for c in exp: 
        if c in("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            continue
        elif c in ("*", "/", "+", "-"):
            o = c
            break
    return o
op1 = op_first_extrct("1235678-16+18")
print(op1)


def calculate1(exp):
    """
    Takes as input an expression containing only numbers (digits) and the following signs:
    +, -, /, x
    It will not contain any other character (including space)
    Example 1: 5-2+4
    Example 2: 123-16+18
    Return the result.
    Follow PEMDAS
    """

    # Your code starts here
    # This is what I am going to do...
    #   e1 = int(input("Put your entire expression: "))
    #   
    #
    # o1 = input("Input your first operand: ")
    #   n2 = float(input("Input your second number: "))
    #   o2 = input("Input your second operand: ")
    #   n3 = float(input("Input your third number: "))
    ## (FOR LATER) chk = input("Do you want more operators? (Y for yes and N for no) ").upper()
    #
    # if o1 in ("*") and o2 in ("+"):
    #   ans_M = (n1*n2)
    #   ans_A = (ans_E+n3)
    #   print = (f"Your answer is {ans_S}")
    # elif o1 in ("/") and o2 in ("+"):
    #   ans_D = (n1/n2)
    #   ans_A2 = (ans_E+n3)
    #   print = (f"Your answer is {ans_S}")                                                                                                   
    # elif o1 in ("*") and o2 in ("-"):
    #   ans_S2 = (ans_M-n3)
    #   print = (f"Your answer is {ans_S}")
    # elif o1 in ("/") and o2 in ("-"):
    #                                                                            
 