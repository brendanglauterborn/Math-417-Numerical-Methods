#Brendan Lauterborn
#726004578
#Math 417 HW4

from scipy.interpolate import CubicSpline
from scipy.interpolate import lagrange
import matplotlib.pyplot as graph
import numpy as np

x=[1,2,5,6,7,8,10,13,17]
y=[3,3.7,3.9,4.2,5.7,6.6,7.1,6.7,4.5]
cs= CubicSpline(x,y)
xs = np.arange(1, 17.5,.5)
graph.plot(x,y,'k',label='data')
graph.plot(xs,cs(xs),'b',label='cubic spline 1')



x2=[17,20,23,24,25,27,27.7]
y2=[4.5,7,6.1,5.6,5.8,5.2,4.1]
cs2=CubicSpline(x2,y2)
xs2=np.arange(17,27.8,.1)
graph.plot(x2,y2,'k',)
graph.plot(xs2,cs2(xs2),'g',label='cubic spline 2')

x3=[27.7,28,29,30]
y3=[4.1,4.3,4.1,3]
cs3=CubicSpline(x3,y3)
xs3=np.arange(27.7,30,.1)
graph.plot(x3,y3,'k',)
graph.plot(xs3,cs3(xs3),'r',label='cubic spline 3')

graph.xlabel('x')
graph.ylabel('f(x)')

graph.figure(2)
graph.plot(x,y,'k',label='data')
xs4 = np.arange(1,14)
graph.plot(xs4,lg(xs4))
graph.plot(x2,y2,'k',label='data')
lg2= lagrange(x2,y2)
graph.plot(xs2,lg2(xs2))
graph.plot(x3,y3,'k',label='data')
lg3= lagrange(x3,y3)
graph.plot(xs3,lg3(xs3))