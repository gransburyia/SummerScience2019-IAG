# -*- coding: utf-8 -*-
"""
Created on Fri May 24 12:46:50 2019

@author: grans
"""
#Constants in the program
a = 0

b = 1

alpha = 1/2

beta = 1/3

n = 1

#function in format bertini will understand
p = "2 * x^3"

def writeInputFile():#v stands for variables, funcs stands for the amount of functions
    inputFile = open("d1Python.txt", "w")
    
    inputFile.write("INPUT\n\n")
    
    inputFile.write("variable_group x;\n\n")
    
    inputFile.write("function f;\n\n")
    
    inputFile.write("constant alpha, beta, a, b, n;\n\n")
    
    alphaString = "alpha = " + str(alpha) + ";\n\n"
    
    inputFile.write(alphaString)
    
    betaString = "beta = " + str(beta) + ";\n\n"
    
    inputFile.write(betaString)
    
    aString = "a = " + str(a) + ";\n\n"
    
    inputFile.write(aString)
    
    bString = "b = " + str(b) + ";\n\n"
    
    inputFile.write(bString)
    
    nString = "n = " + str(n) + ";\n\n"
    
    inputFile.write(nString)
    
    inputFile.write("h = ((b-a)/n+1);\n\n")
    
    inputFile.write("f = alpha - 2 * x + beta - h^2 * (" + p + ");\n\n")
    
    inputFile.write("END;")
    
writeInputFile()
