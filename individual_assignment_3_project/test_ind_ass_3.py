# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:36:06 2018

@author: Grani
"""


from individual_assignment_3 import recalculate_quality
from individual_assignment_3 import Product

potato = Product("potato", 6)
cheese = Product ("cheese", 6)
apple = Product("apple", 3)
corn = Product("corn", 6)

product_list = [potato, cheese, apple, corn]

changed_quality = [5.5, 4, 0, 6]
 
product_quality = []
 
def test_recalculate_quality():
    for product in product_list:
        recalculate_quality(product)
        product_quality.append(product.quality)
        
    assert changed_quality == product_quality
        


