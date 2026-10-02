# Types of lines
# Normal lines:
def line(n):
    for i in range(n):
        print("* ", end="")

def line_wthut_spcs(n):
    for i in range(n):
        print("*", end="")

# Line's with spaces in between them
def e_line(e):
    for i in range(0,e):
        if i == 0 or i == e-1:
            print ("* ", end="")
        else:
            print("  ", end="")

def e_line_without_space(e):
    for i in range(0,e):
        if i == 0 or i == e-1:
            print ("*", end="")
        else:
            print("  ", end="")


# Write a function named (print_triangle_left_aligned())
# Example Input: 3 (integer)
# Example output:
# * * *
# * *
# *

# line(9)

# This triangle prints like this:
# input == 3
# output:
# * * *
# * *
# *
# Note: only works for {line()}, {e_line()}
def print_triangle_left_aligned(m):
    for i in range(m):
        line(m-i)
        print("")

# print_triangle_left_aligned(7)
# Below is for experimenting

def experimenting_w_triangles(m):
    for i in range(m):
        if i == 0 or m:
            line(m-1)
        else:
            line(m-1)
        print("")

# experimenting_w_triangles(6)

# Middle triangle (only for one space lines):
# Input == 7
# Output:
# * * * * * * * 
#  * * * * * * 
#   * * * * * 
#    * * * * 
#     * * * 
#      * * 
#       * 
def middle_triangle(m):
    for i in range(m):
        for j in range(i):
            print(" ", end="")
        line(m-i)
        print("")

# This triangle prints like this:
# input == 3
# output:
# * * *
#   * *
#     *
# Note: there must be a space for each variable in the line including spaces
def print_triangle_right_aligned(m):
    for i in range(m):
        for j in range(i):
            print("  ", end="")
        line(m-i)
        print("")
        
        
# print_triangle_right_aligned(7)
# Work in progress

#k = input ("Give me a number here (odd numbers only) -----> ")
#  *
# ***
#***** 
def normal_triangle(m):
    l = (m+1)/2
    p = int(l) #had to make int because whenever you divide python automatically converts to a float
    k = (m-1)/2
    o = int(k) #footnote above
    for i in range(p):
        for j in range(o):
            print(" ", end="")
        o = o-1
        line_wthut_spcs(i*2+1)
        print("")

#n = int(k)
#normal_triangle(n)

def calculator():
    equation = input ("Select your symbol (+,-,*,/) ----> ")
    if equation == "+":
        a = float(input("Input first number here: "))
        a2 = float(input("Input second number here: "))
        ans_a = a + a2
        trl_a = input("Do you want more values?(Say Y for yes and N for no) ").upper()
        while trl_a == "Y":
            a2 = float(input("Input number here: "))
            ans_a = ans_a + a2
            trl_a = input("Do you want more values?(Say Y for yes and N for no) ").upper()
        if trl_a == "N":
            print(f"Your answer is {ans_a}")
    elif equation == "-":
        s = float(input("Input your first number here: "))
        s2 = float(input("Input your second number here: "))
        trl_s = input("Do you want more values?(Say Y for yes and N for no) ").upper()
        ans_s = s - s2
        while trl_s == "Y":
            s2 = float(input("Input number here: "))
            ans_s = ans_s - s2
            trl_s = input("Do you want more values?(Say Y for yes and N for no) ").upper()
        if trl_s == "N":
            print(f"Your answer is {ans_s}")
    elif equation == "*":
        m = float(input("Input your first number here: "))
        m2 = float(input("Input your second number here: "))
        trl_m = input("Do you want more values?(Say Y for yes and N for no) ").upper()
        ans_m = m * m2
        while trl_m == "Y":
            m2 = float(input("Input number here: "))
            ans_m = ans_m * m2
            trl_m = input("Do you want more values?(Say Y for yes and N for no) ").upper()
        if trl_m == "N":
            print(f"Your answer is {ans_m}")
    elif equation == "/":
        d = float(input("Input your first number here: "))
        d2 = float(input("Input your second number here: "))
        trl_d = input("Do you want more values?(Say Y for yes and N for no) ").upper()
        ans_d = d / d2
        while trl_d == "Y":
            d2 = float(input("Input number here: "))
            ans_d = ans_d / d2
            trl_d = input("Do you want more values?(Say Y for yes and N for no) ").upper()
        if trl_d == "N":
            print(f"Your answer is {ans_d}")

    else:
        print("Some parts are still not finished or you have attempted to put some malicious code or you put random stuff :p")
        print("System_self_destruct_in_progress...")
        exit()

calculator()

