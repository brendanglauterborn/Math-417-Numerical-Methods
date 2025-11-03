#Brendan Lauterborn
#Math 417 Midterm Question 6


def mult(v1,v2):
    if (len(v1) > 1 and v1[-1]==0) or (len(v2) > 1 and v2[-1]==0) or len(v2) > 2:
        print("invalid")
        return
    result = [0]*(len(v1)+len(v2)-1)
    for i  in range(len(v1)):
        for j in range(len(v2)):
            result[i+j] += v2[j]*v1[i]
    #print(result)
    return result

def add(v1,v2):
    #if (len(v1) > 1 and v1[-1]==0) or (len(v2) > 1 and v2[-1]==0):
     #   print("invalid")
      #  return    
    length = max(len(v1),len(v2))
    result = [0]*length
    for i in range(len(v1)):
        result[i] = v1[i]
    for i in range(len(v2)):
        result[i] += v2[i]
    while result[-1] == 0:
        result.pop()
    #print(result)
    return result
    
def lagrange(x,k):
    if (len(x) > 1 and x[-1]==0) or (not isinstance(k,int)) or (k>len(x)):
        print("invalid")
        return
    d = 1
    a = []
    for i in range(len(x)):
        if i != k:
            d *= x[k] - x[i]
            a.append(x[i])
        
    b = [a[0]*-1,1]

    for i in range(1,len(a)):
        c = [a[i]*-1, 1]
        temp=[0]*(len(b)+1);
        for j in range(len(b)):
            for k in range(len(c)):
                temp[j+k] += b[j]*c[k]
        
        b = temp
    result=[i / d for i in b]
    #print(result)
    return result
    

def interpolate(x,f):
 
    temp=[0]*len(x)
    for i in range(len(x)):
        a = lagrange(x,i)
        a1=[k*f[i] for k in a]
        for j in range(len(temp)):
            temp[j]+=a1[j]
    print(temp)  
    
x=[0,1,3,2,5]
y=[0,1]
print(mult(x,y))
x=[3,0,1]
y=[3]
print(mult(x,y))
x=[0,0,0,0,0,1]
y=[3,5]
print(mult(x,y))


x=[0,1,3,2,5]
y=[0,1]
print(add(x,y))
x=[3,0,1]
y=[3]
print(add(x,y))
x=[0,3,7,5]
y=[1,0,-7,-5]
print(add(x,y))

x=[0,1,2,3]
k=0
print(lagrange(x,k))
x=[.5,.7,3,4]
k=3
print(lagrange(x,k))
x=[0,1]
k=1
print(lagrange(x,k))


x=[0,1,2,3]
f=[0,1.5,70,3]
interpolate(x,f)
x=[-10,0,3,5]
f=[0,1,2,3]
interpolate(x,f)
x=[-5,-3,-1,1,3,5]
f=[11,12.5,14,15.5,17,18.5]
interpolate(x,f)
x=[-5,-3,-1,1,3,5]
f=[11,12.5,14,15,17,18.5]
interpolate(x,f)
x=[500,501,502,503]
f=[0,1.5,70,3]
interpolate(x,f)

