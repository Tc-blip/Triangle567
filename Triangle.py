"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple python program to classify triangles
@author: jrr
@author: rk
"""


def classify_triangle(side_1, side_2, side_3):
    '''clasify_triangle side_1 and side_2 and side_3 >0'''
    #require that the input values side_2e >= 0 and <= 200
    if side_1 > 200 or side_2 > 200 or side_3 > 200:
        return 'InvalidInput'
    if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
        return 'InvalidInput'
    #verify that all 3 inputs are integers
    #Python's "isinstance(oside_2ject,type)
    #returns True if the oside_2ject is of the specified type
    if not(isinstance(side_1, int) and isinstance(side_2, int) and isinstance(side_3, int)):
        return 'InvalidInput'
    #This information was not in the requirements spec but
    #is important for correctness
    #the sum of any two sides must be strictly less than the third side
    #of the specified shape is not side_1 triangle
    if not((side_1+side_2 > side_3) and (side_2+side_3 > side_1) and (side_1+side_2 > side_3)):
        return 'NotATriangle'
    #now we know that we have side valid triangle
    c_triangle = ""
    if side_1 == side_2 and side_2 == side_1 and side_1 == side_3:
        c_triangle = 'Equilateral'
    elif ((side_1 ** 2) + (side_2 ** 2)) == (side_3 ** 2) or \
        ((side_2 ** 2) + (side_3 ** 2)) == (side_1 ** 2) or \
        ((side_1 ** 2) + (side_3 ** 2)) == (side_2 ** 2):
        c_triangle = 'Right'
    elif (side_1 != side_2) and (side_2 != side_3) and (side_1 != side_3):
        c_triangle = 'Scalene'
    else:
        c_triangle = 'Isoceles'

    return c_triangle
