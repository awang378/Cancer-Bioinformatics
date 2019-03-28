# -*- coding: utf-8 -*-
"""
Data Visualization Test
Created on Sat Feb 23 14:23:11 2019

@author: Andrew
"""

import matplotlib.pyplot as plt
import numpy as np
import csv

with open("cancerdata.csv") as file:
    reader = csv.DictReader(file)
    cancer = [dict(line) for line in reader]

data = {"x": [], "y": [], "label": [], "color": [], "scale": []}
for entry in cancer:
    data["x"].append(entry["Mutation to Gene"])
    data["y"].append(entry["Survival Estimate"])
    data["label"].append(entry["Primary Site"])
    if entry["Primary Site"] == "Colon":
        data["color"].append("red")
    elif entry["Primary Site"] == "Breast":
        data["color"].append("green")
    else:
        data["color"].append("blue")
    data["scale"].append(float(entry["Percent Affected"])*10000)
    
    

plt.figure(figsize = (10,8))

plt.title("Data Visualization", fontsize = 20)
plt.xlabel("Mutations per gene", fontsize = 15)
plt.ylabel("Survival Estimate", fontsize = 15)
plt.scatter(x=[float(x) for x in data["x"]], y=[float(y) for y in data["y"]], 
               s=data["scale"], c=data["color"], alpha = 0.3)
plt.show()


    
    
    