##coding=utf8
##author=Sanhe
##date=07-13-2014

import numpy as np

'''
=== PROBLEM 01 ===
Suppose we have 4 students and a classroom with 4 seats.
In semester 2011 Fall, they have took 6 exams. They randomly
pick seats in each exam.

Suppose the score of the 4 students in these 6 exam obeying
normal distribution.

student1 ~ N(84,9)
student2 ~ N(92,4)
student3 ~ N(75,16)
student4 ~ N(87,16)

please generate a data sheet indicate the scores 
        exam1    exam2    exam3    exam4    exam5    exam6
seat1       
seat2
seat3                scores
seat4
'''

def problem1(number_of_student, number_of_exam): ## <=== INSERT YOUR CODES HERE
    data = np.array([np.random.randn(number_of_exam) * 3 + 84, ## generate N(84,9) from N(0,1) * 3 + 84
                     np.random.randn(number_of_exam) * 2 + 92,
                     np.random.randn(number_of_exam) * 4 + 75,
                     np.random.randn(number_of_exam) * 4 + 87])

    newdata = np.array([data.transpose()[0][ np.random.permutation(number_of_student) ], ## permulation
                        data.transpose()[1][ np.random.permutation(number_of_student) ],
                        data.transpose()[2][ np.random.permutation(number_of_student) ],
                        data.transpose()[3][ np.random.permutation(number_of_student) ],
                        data.transpose()[4][ np.random.permutation(number_of_student) ],
                        data.transpose()[5][ np.random.permutation(number_of_student) ]]).transpose() ## transpose back
    return newdata

if __name__ == '__main__':
    print '\nProblem1 Result:\n%s' % problem1(4,6)