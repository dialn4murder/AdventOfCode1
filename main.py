
import numpy

# Loads text file into input 1 and 2, .T Makes it into columns
input1, input2 = numpy.loadtxt("text.txt", int).T

# Sort the input
input1 = numpy.sort(input1)
input2 = numpy.sort(input2)

# Print the difference, abs makes it not negative
print (sum(abs(input2-input1)))