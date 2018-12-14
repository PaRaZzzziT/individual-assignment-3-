# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:53:59 2018

@author: Grani
"""

import requests

phonebook = {
        "Dani": "79060485763"
}

localhost = ""


def show_phonebook():
    response = requests.get(localhost + "/phonebook")
    if response.status_code == 200:
        return response.json()
    else:
        return "I'm calling police"
    
def add_contact(name, phone):
    response = requests.post(localhost + "/addcontact/" + name + "/" + phone)
    if response.status_code == 200:
        return response.json()
    else:
        return "I'm calling police"

def show_contact(name):
    response = requests.get(localhost + "/showcontact/" + name)
    if response.status_code == 200:
        return response.json()
    else:
        return "I'm calling police"
    
def del_contact(name):
    response = requests.post(localhost + "/removecontact/" + name)
    if response.status_code == 200:
        return response.json()
    else:
        return "I'm calling police"
    
    
    
def update_contact(name, phone):
    response = requests.post(localhost + "/updatecontact/" + name + "/" + phone)
    if response.status_code == 200:
        return response.json()
    else:
        return "I'm calling police"