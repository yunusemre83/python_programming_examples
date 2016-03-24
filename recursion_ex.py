# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:11:24 2016

@author: yemre
"""

import numpy as np
import functools

'''
## Fibonacci
def fibonacci(val):
    
    if (val==0 or val==1):
        return 1
    else:
        return fibonacci(val-1)+fibonacci(val-2)
        
for i_val in range(10):
    print('fibonacci {}:{}'.format(i_val,fibonacci(i_val)))        


    
## Min steps   
sequence=[1,2,4,8]
target=73
max_val = target+1
#@functools.lru_cache(maxsize=None)

calc_step_cache=max_val*np.ones((max_val+np.max(sequence),max_val+np.max(sequence),np.max(sequence)+1))
def calc_step(num_steps,acc_value,cur_val):    
    
    num_steps = num_steps+1
    acc_value = acc_value+cur_val

    if(calc_step_cache[num_steps,acc_value,cur_val]!= max_val):
        return calc_step_cache[num_steps,acc_value,cur_val]
    
    if (acc_value == target):
        calc_step_cache[num_steps,acc_value,cur_val] = num_steps
        return num_steps
    elif (acc_value > target):
        calc_step_cache[num_steps,acc_value,cur_val] = max_val
        return max_val
    else:
        calc_step_cache[num_steps,acc_value,cur_val] = np.min([calc_step(num_steps,acc_value,i_val) for i_val in sequence])
        return calc_step_cache[num_steps,acc_value,cur_val] 

result = np.int(np.min([calc_step(0,0,i_val) for i_val in sequence]) )     
'''

'''  
def put_a_char(s):
    out=[]
    if(len(s)==1):
        return [s]
    else:
        for i_val,i_str in enumerate(s):
            s_new = s[0:i_val]+s[(i_val+1):]
            for i_rec_str in put_a_char(s_new):
                out+=[i_str+i_rec_str]

    return out        

result = put_a_char('abcef')
'''



def reverse(s):
    
    # Base Case
    if len(s) <= 1:
        return s

    # Recursion
    return reverse(s[1:]) + s[0]
    
print(reverse('hello world'))  