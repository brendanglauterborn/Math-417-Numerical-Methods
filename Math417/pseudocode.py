#Brendan Lauterborn
#Math 417 Midterm Question 6

'''
a)

I will first create the function called mult where i will take in v1 and v2. Next i will check for the unique correspondence condition. If that is not met we will return invalid. If it is met, we will continue. Next i will create a reulting vector consisting of 0's of size size v1 + v2 -1. I will then create a nested loop to multiply each term of v2 with each term of v1 and set that equal to the resulting vector. Finally we create all of the variables that will need to be called. After that we will call the function with the correct arguments. The resulting vectors will then be printed.

b)
I will first create the add function which brings in v1 and v2. I will check for the unique correspondence condtition. If not met we print error. if met the coode continues. I then create the resulting vector by creating a vector of 0s of length max(v1,v2).I then set the ith terms in the resulting matrix to be equal to the ith terms of v1 via for loop. Next I will add v2 to the resulting matrix. After that we do not want any trailing 0's so i will create a while loop and index backwards to delete any trailing 0's. After this we have our resulting matrix. I now have to define the variables that I will call and call the function with the appropriate arguments.

c)
First i will calculate the denominator and add all x's except the kth. This is done by looping through the ith terms in x != k and subtracting the correct values. I will then make a vector b which will be set to -1 times x in the 0th term , 1. Then i will define c to be a vector = [-x_1,1]. The one in the second position corresponds to the x when multiplying. Each vector will be in increasing order of degree. After this i will Calculate the coefficients for the numerator: loop through each vector, find the index of the resultant vector (temp), calculate the product of the values at each index, and add that to the resultant vector at the calculated index. Next i will update b by setting it equal to temp. and print b / denominator which is the resulting coeff.


d)I will call the lagrange function and multply each L_i by f(x_i) by looping the size of x. then i will add all of the terms up while storing the previous value in temp and then += the new value for the ith L. then print the result
'''
