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

k = input ("Give me a number here -----> ")
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

n = int(k)
normal_triangle(n)
