# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:25:32 2016

@author: yemre
"""

import numpy as np

def binary_search(arr,val):
    start_x = 0
    last_x = len(arr)-1
    found_val = False
    
    while (not found_val) and (last_x >= start_x):
        mid_x = int((last_x + start_x + 1)/2)
        
        print(start_x,mid_x,last_x)
        
        if (arr[mid_x]==val):
            found_val = True
        else:
            if(arr[mid_x]>val):
                last_x = mid_x -1
            else:
                start_x = mid_x +1
         
    return [found_val,mid_x]

def bubble_sort(arr):
    
    arr_len = len(arr)
    
    for i in range(arr_len):
        for j in range(arr_len-i-1):
            if (arr[j] > arr[j+1]):
                temp_val = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp_val
    return arr           

def insertion_sort(arr):
   
    arr_len = len(arr)
    
    for i in range(1,arr_len):
        
        cur_val = arr[i]
        pos = i
        while (pos > 0 and (cur_val < arr[pos-1])):
            arr[pos]=arr[pos-1]
            arr[pos-1]=cur_val
            pos=pos-1

    return arr           


def comp_selection_sort(arr):
    
    arr_len = len(arr)
    
    for i in range(arr_len):
        for j in range(i+1,arr_len):
            if (arr[i]>arr[j]):
                temp_val = arr[i]
                arr[i]=arr[j]
                arr[j]=temp_val
    return arr           

def selection_sort(arr):
    
    arr_len = len(arr)
    
    for i in range(arr_len):
        min_val = arr[i]
        min_pos = i
        for j in range(i+1,arr_len):
            if (min_val > arr[j]):
                min_val = arr[j]
                min_pos = j
        if (min_pos != i):
            temp_val = arr[i]
            arr[i]=min_val
            arr[min_pos]=temp_val
    return arr           
       
def merge_sort(arr):
    
      
    def split(arr,first,last):
        
        if (last-first == 0):
            return [arr[first]]
        else:    
            mid = int((last+first-1)/2)
            print(first,mid,last)
            arr_a = split(arr,first,mid)
            arr_b = split(arr,mid+1,last)
            return merge (arr_a,arr_b)

    def merge (arr_a,arr_b):
        out_arr = []
        
        a_ptr = 0
        b_ptr = 0
        mid = len(arr_a)
        last = len(arr_b)
        out_ptr = 0
        
        while (a_ptr < mid and b_ptr < last):
            if (arr_a[a_ptr] > arr_b[b_ptr]):
                out_arr.append(arr_b[b_ptr])
                b_ptr = b_ptr + 1
            else:
                out_arr.append(arr_a[a_ptr])
                a_ptr = a_ptr + 1
            out_ptr = out_ptr + 1
        
        if (a_ptr == mid):
            for b_next in range(b_ptr,last):
                out_arr.append(arr_b[b_next])

        if (b_ptr == last):
            for a_next in range(a_ptr,mid):
                out_arr.append(arr_a[a_next])          
        
        return out_arr
     
    arr_len = len(arr)
    return split(arr,0,arr_len-1)


def quick_sort_call(arr):
    arr_len = len(arr)
    quick_sort(arr,0,arr_len-1)
    return arr

def quick_sort(arr,first,last):
    
    if (last < first):
        return
    
    def splitdata(arr_in,in_first,in_last):
        
        left_mark = in_first
        right_mark = in_last-1
        split_value = arr[in_last]
        finish_proc = False
        
        while ((not finish_proc) and (right_mark >= left_mark)):
            
            while (left_mark <= right_mark and arr_in[left_mark]<=split_value):
                left_mark = left_mark + 1

            while (left_mark <= right_mark and arr_in[right_mark]>=split_value):
                right_mark = right_mark - 1
                
            if (left_mark > right_mark):
                finish_proc = True
            else:
                temp_val = arr[right_mark];
                arr_in[right_mark] = arr_in[left_mark]
                arr_in[left_mark] = temp_val
        
        temp_val = arr_in[left_mark]
        arr_in[left_mark] = split_value
        arr_in[in_last]=temp_val


        return left_mark        
                
    splitpoint = splitdata(arr,first,last)
    
    quick_sort(arr,first,splitpoint-1)
    quick_sort(arr,splitpoint+1,last)
                
                
my_arr = np.random.randint(0,10,7)
print('arr: {}'.format(my_arr))
my_arr_sorted = insertion_sort(my_arr)
print('sorted arr: {}'.format(my_arr_sorted))
target_val = 5
print(binary_search(my_arr,target_val))



    