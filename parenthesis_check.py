# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 10:28:55 2016

@author: yemre
"""


def paranthesis_check(s):

    opening_char = '({['
    closing_char = ')}]'
    sstack = []
    
    for s_val in s:
        if s_val in opening_char:
            sstack.append(s_val)
        elif s_val in closing_char:
            if (len(sstack)==0):
                return False
            s_pop = sstack.pop()
            
            if (str.find(closing_char,s_val) != str.find(opening_char,s_pop)):
                return False
        else:
            print('ERROR: Unexpected char')
            return False
        
    if (len(sstack)!=0):
        return False
    
    return True
    
test_string='({})[]{()}'    
print('{} {}'.format(test_string,paranthesis_check(test_string)))        

test_string='({}[)]'    
print('{} {}'.format(test_string,paranthesis_check(test_string)))    