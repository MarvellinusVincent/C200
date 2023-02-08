# Put all your code for the Final exam in this file
# Make sure that you test your code before submission.

# Due to time constraints, there won't be grade review for the coding portion of the 
# exam so ensure that your submission is correct and run without errors.

# This file is left empty intentionally, you can use the code from the PDF as a starting point.
import numpy as np

class Triangle:
    def __init__(self,p=[]):
        self.__p = np.array(p)

    def area_d(self):
        d_ = []
        for i in range(3):
            d_.append([i for i in self.__p[i]]+[1])
        return round(abs(np.linalg.det(np.array(d_)))/2,2)

    def distance(self,p0,p1):
        x0,y0 = self.__p[p0]
        x1,y1 = self.__p[p1]
        return ((x0-x1)**2 + (y0-y1)**2)**(1/2)

    def herron(self):
        a = self.distance(0,1)
        b = self.distance(1,2)
        c = self.distance(0,2)

        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        return round(area,2)

    def __eq__(self,other):
        return self.area_d() == other.area_d()

t = Triangle([[-2,2], [1,5], [6,1]])
s = Triangle([[4,4], [2,-2], [-4,0]])
r = Triangle([[-1,1],[2,6],[7,1]])
print(t.area_d())
print(r.area_d())
print(s.area_d())
print(t.herron())
print(r.herron())
print(s.herron())
print(t == r)
print(r == s)