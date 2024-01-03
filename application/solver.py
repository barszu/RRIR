import numpy as np
import math
from scipy import integrate

# ------------------------------------------------------
# e functions
def e(i:int, x):
    if x < h * (i - 1) or x > h * (i + 1):
        return 0
    if x < h * i:
        return x / h - i + 1
    return - x / h + i + 1

def e_derivative(i:int, x):
    if x < h * (i - 1) or x > h * (i + 1):
        return 0
    if x < h * i:
        return 1 / h
    return -1 / h

# ------------------------------------------------------
# B , L (tylda) functions

def B(i:int, j:int): #== -integral(from=0 , to=3 , function= e'i * e'j)
    if abs(i-j) >=2 : return 0 #integral from e'i * e'j === 0 
    elif abs(i-j) == 1 :
        if not i < j : #swap, i-th always on left
            i , j = j , i 
        # i | j = i+1 !
        # ei * ej === 0 when x not in [i*h , (i+1)*h] (common space beetween ei , ej)
        integral_start = i*h
        integral_end = (i+1)*h # i+1 * h
        # integrate.quad -> [res , error_margin]
        return - integrate.quad(lambda x: e_derivative(i,x) * e_derivative(j,x) , integral_start , integral_end )[0]    
    else: # i == j
        # ei ^ 2 === 0 when x not in [(i-1)*h , (i+1)*h] (mountain space)
        integral_start = (i-1)*h
        integral_end = (i+1)*h
        # integrate.quad -> [res , error_margin]
        return - integrate.quad(lambda x: e_derivative(i, x) ** 2, integral_start , integral_end)[0]

def L(j:int): #== -integral(from=1 , to=2 , function= ej)
    integral_start = 1.0
    integral_end = 2.0
    # not integrating 0 !!! -> ej === 0 on [integral_start , integral_end]
    if (j+1)*h < integral_start or (j-1)*h > integral_end: return 0
    return 4*math.pi*G* integrate.quad(lambda x: e(j, x), integral_start , integral_end)[0]

# ------------------------------------------------------
# extra functions

def shifter(x): #shift fun aka u_tylda
    return -1/3 * x + 5

# ------------------------------------------------------
# solver, main fun

def solve(elem_no:int,G_fromUI:float,draw_samples:int):
    global h
    global G
    
    G = G_fromUI
    
    h = 3 / elem_no
    
    # solving for w!! u=up + w
    MainMatrix = [[B(i,j) for j in range(1,elem_no)] for i in range(1,elem_no)]
    MainMatrix = np.array(MainMatrix)
    
    ResMatrix = [L(j) for j in range(1,elem_no)]
    ResMatrix = np.array(ResMatrix)
    
    # w = w0*e0 + w1*e1 + ... + wn-1*en-1 + wn * en | w(0) = 0 , w (3) = 0 |=> w = w1*e1 + ... + wn-1*en-1
    w_scalars:list = [0.0] + np.linalg.solve(MainMatrix, ResMatrix).tolist() + [0.0] #<- wi
    
    def w(x): # E wi * ei(x)
        nonlocal w_scalars
        res = 0.0
        for i in range(1 , elem_no):
            res += w_scalars[i] * e(i,x)
        return res
        
    x_es:list = [3/draw_samples * k for k in range(draw_samples+ 1)]
    y_es:list = [ w(x) + shifter(x)  for x in x_es]
    
    return (x_es, y_es)
