# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:42:13 2017

@author: nattawutvejkanchana
"""

from days import *

def without_keys(d, keys):
    return {k: v for k, v in d.items() if k not in keys}
    
def sum_we():
    return sum([ ppl_we.get(k) for k in ppl_we.keys()])
    
def sum_wd():
    return sum([ ppl_wd.get(k) for k in ppl_wd.keys()])
    
def get_max_pname(in_dict,except_keys = []):
    new_dict = without_keys(in_dict, except_keys)
    return max(new_dict, key=in_dict.get)
    
def assign_dict_we(date):
    global n_we_assigned
    pname = get_max_pname(ppl_we)
    pos_left = sum_we()
    
    day_list[date] = (pname,None)
    ppl_we[pname] = ppl_we[pname] - 1
    
    #if position is not enough so assign two pos
    if pos_left > (n_we - n_we_assigned):
        pname2 = get_max_pname(ppl_we)
        day_list[date] = (pname,pname2)
        ppl_we[pname2] = ppl_we[pname2] - 1
    
    n_we_assigned = n_we_assigned + 1
    
def assign_dict_wd(date):
    global n_wd_assigned,day_list
    not_eligible_pname = []
    if day_list[date + 1] is not None:
        not_eligible_pname.extend(list(day_list[date+1]))
    if day_list[date - 1] is not None:
        not_eligible_pname.extend(list(day_list[date-1]))
    
    #print(not_eligible_pname)
    pname = get_max_pname(ppl_wd,not_eligible_pname)
    pos_left = sum_wd()
    
    day_list[date] = (pname,None)
    #print(day_list)
    ppl_wd[pname] = ppl_wd[pname] - 1
    
    #if position is not enough so assign two pos
    if pos_left > (n_wd - n_wd_assigned):
        pname2 = get_max_pname(ppl_wd,not_eligible_pname)
        day_list[date] = (pname,pname2)
        ppl_wd[pname2] = ppl_wd[pname2] - 1
    
    n_wd_assigned = n_wd_assigned + 1
    
    
    
    

dates_in_month = get_dates_in_month(2017,3) #year, month
N_DAYS = len(dates_in_month)
ppl = ['A','B','C','D'] #people

we = [i for i in range(0,len(dates_in_month)) if not is_weekday(dates_in_month[i]) ]
wd = [i for i in range(0,len(dates_in_month)) if i not in we ]

n_wd = len(wd)
n_we = len(we)
n_wd_assigned = 0
n_we_assigned = 0

ppl_we = {}
ppl_wd = {}
for p in ppl:
    ppl_we[p] = 3
    ppl_wd[p] = 7

day_list = [ None for i in range(0,N_DAYS)]
for i in we:
    assign_dict_we(i)

#for i in wd:
#    not_empty = [i for i in range(0,N_DAYS) if day_list[i] is not None ]
#    not_none_date = min(not_empty)
#    if day_list[not_none_date - 1] is None:
#        date = not_none_date - 1
#    
#    print(date)
#    assign_dict_wd(date)

while(True):
    not_empty = [i for i in range(0,N_DAYS) if day_list[i] is not None ]
    empty = [i for i in range(0,N_DAYS) if day_list[i] is None ]
    if len(empty) == 0:
        break
    while(True):
        not_none_date = empty.pop(0)
        if not_none_date - 1 >= 0:
            if day_list[not_none_date - 1] is None:
                date = not_none_date
                break
        if not_none_date + 1 <= N_DAYS - 1:
            if day_list[not_none_date + 1] is None:
                date = not_none_date
                break
        if len(empty) == 0:
            print('ERROR')
            break
    assign_dict_wd(date)
