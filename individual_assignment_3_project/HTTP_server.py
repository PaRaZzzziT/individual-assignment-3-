# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:53:26 2018

@author: Grani
"""

from flask import Flask, jsonify

phonebook = {
        "Dani": "79060485763"
}


server = Flask("Phonebook")

@server.route("/phonebook", methods = ["GET"])
def show_phonebook():
    return phonebook

@server.route("/addcontact/<name>/<phone>", methods = ["POST"])
def add_contact(name, phone):
    temp_book = {name: phone}
    phonebook.update(temp_book)
    print("Contact added!")
    
@server.route("/showcontact/<name>", methods = ["GET"])
def show_contact(name):
    if name in phonebook:
        print(name + ": " + phonebook[name])
    else:
        print("There is no such contact in the phonebook")

@server.route("/removecontact/<name>", methods = ["POST"])
def del_contact(name):
    if name in phonebook:
        del phonebook[name]
        print("The contact has been deleted!")
    else:
        print(name + " is not in the phonebook")
        
@server.route("/updatecontact/<name>/<phone>", methods = ["POST"])
def update_contact(name, phone):
    if name in phonebook:
        phonebook[name] = phone
        print("The contact has been updated!")
    else:
        print("There is no such contact in the phonebook")
        
server.run()
        
        
        
        
        