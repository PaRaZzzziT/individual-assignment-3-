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

@server.route("/phonebook")
def show_phonebook():
    return jsonify(phonebook)

@server.route("/addcontact/<name>/<phone>")
def add_contact(name, phone):
    temp_book = {name: phone}
    phonebook.update(temp_book)
    return jsonify("Contact added!")
    
@server.route("/showcontact/<name>")
def show_contact(name):
    if name in phonebook:
        return jsonify(name + ": " + phonebook[name])
    else:
        return jsonify("There is no such contact in the phonebook")

@server.route("/removecontact/<name>")
def del_contact(name):
    if name in phonebook:
        del phonebook[name]
        return jsonify("The contact has been deleted!")
    else:
        return jsonify(name + " is not in the phonebook")
        
@server.route("/updatecontact/<name>/<phone>")
def update_contact(name, phone):
    if name in phonebook:
        phonebook[name] = phone
        return jsonify("The contact has been updated!")
    else:
        return jsonify("There is no such contact in the phonebook")
        
server.run()
        
        
        
        
        