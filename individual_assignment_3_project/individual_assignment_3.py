# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:35:03 2018

@author: Grani
"""
#%%
class Product:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality
        

def recalculate_quality(product):
    if product.name == "potato":
        product.quality = product.quality - 0.5
    elif product.name == "cheese":
        product.quality = product.quality - 2
    else:
        if product.quality < 5:
            product.quality -= 3
            
#%%

import requests

def discription_of_repos():
    response = requests.get("https://api.github.com/users/PaRaZzzziT/repos").json()
    
    for repository in response:
        if repository["description"] != None:
            print(repository["name"] + ": " + str(repository["description"]) + ". Has " + str(repository["stargazers_count"]) + " star(s), and is written in " + str(repository["language"]) + ". URL: " + repository["html_url"])
        else:
            print(repository["name"] + ". Has " + str(repository["stargazers_count"]) + " star(s), and is written in " + str(repository["language"]) + ". URL: " + repository["html_url"])

