#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:39:14 2020

@author: aditya
"""

from FlagsNArgs import look_for_arguments, look_for_flags
from Search_scrape import search_scrape
from scrap import search_game
from Game import Game


def Search(inp):
    flag_list = set_search_flags((look_for_flags(inp)))
    name = look_for_arguments(inp)
    if(crackninjaSearch(name,0,flag_list[0],flag_list[1],flag_list[2],flag_list[3],flag_list[4],flag_list[5])):
        return 1
    return 0



def set_search_flags(flags):
    flags_of_search = ["a","i","c","n","r","u"]
    num_flags_of_search = 6
    flag_list = [True,True,True,True,True,True]
    flagset_list = [False,False,False,False,False,False]
    for f in flags:
        #print(f)
        for i in range (num_flags_of_search):
             if (f == flags_of_search[i]):
                if (i%2 ==0):
                    flag_list[i] = True
                    flagset_list[i] = True
                    flag_list[i+1] = not(flagset_list[i] ^ flagset_list[i+1])
                else:
                    flag_list[i] = True
                    flagset_list[i] = True
                    flag_list[i-1] = not(flagset_list[i] ^ flagset_list[i-1])
    return flag_list



def crackninjaSearch(name,number =10,is_aaa = True, is_indie =True, is_cracked = True, is_notcracked = True, is_released = True, is_unreleased = True ):
    # print("You are trying to run SEARCH")
    # print("for",name)
    # print("with the following filters:")
    # print("is_aaa = ",is_aaa)
    # print("is_Indie = ",is_indie)
    # print("is_cracked = ",is_cracked)
    # print("is_not-cracked = ",is_notcracked)
    # print("is_released = ",is_released)
    # print("is_unreleased = ",is_unreleased)
    
    #yaha pe pura scrapping vagera call hoga 
    if(is_aaa and is_indie):
        gtype = 0
    elif(is_aaa):
        gtype = 1
    elif(is_indie):
        gtype = 2
        
    if(is_cracked and is_notcracked):
        gstatus = 0
    elif(is_cracked):
        gstatus = 1
    elif(is_notcracked):
        gstatus = 2
    
    if(is_released and is_unreleased):
        grel_d = 0
    elif(is_released):
        grel_d = 1
    elif(is_unreleased):
        grel_d = 2

        
    ans = search_scrape(name,gstatus,grel_d,gtype)
    display = {}
    i = 1
    for a in ans.keys():
        display[i] = a
        i = i+1
    
    for dk, dv in display.items():
        print(dk,"-->",dv)

    print("Choose the index of the Game you want to checkout : ")        
    choice = input()
    while (int(choice) < 0 or int(choice) >= i):
        print("Sorry, Please make a VALID choice !")
        choice = input()
    
    link = ans[display[int(choice)]]
    
    game_res = search_game(link)
    game_res.printdetails()
    
    return 1
