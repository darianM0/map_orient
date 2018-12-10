import os
import sys
import math
import numpy as np
import pandas as pd
import json

def track_circuits():
    print(os.getcwd())
    with open("C:\\Users\\Darian\\code\\practice\\circuit_points.geojson") as c:
        circuits = json.load(c)

    circuit_locs = []

    for i in circuits["features"]:
        c_name = i["properties"]["NAME"]
        c_coor = i["geometry"]["coordinates"]
        circuit_locs.append([c_name,c_coor])

    print(len(circuit_locs))
    return circuit_locs
        
def t_map_data():
    with open("C:\\Users\\Darian\\code\\practice\\mapping_points.geojson") as t:
        t_map = json.load(t)

    tmap_locs = []
    for i in t_map["features"]:
        t_id = i["properties"]["id"]
        for j in i["geometry"]["coordinates"][0]:
            tmap_locs.append(j[0:2])
    print(len(tmap_locs))
    return tmap_locs

def closest(c_loc,t_loc):
    neighbors = []
    n=0
    for i in c_loc:
        nbr = 10**8
        # print("i = ", i)
        neighbors.append([0,0,0])
        for j in t_loc:
            # print("j = ", j)
            a = j[0] - i[1][0]
            b = j[1] - i[1][1]
            c = math.sqrt(a**2+b**2)
            
            if c < nbr:
                nbr = c
                # print(c)
                neighbors[n][0:2] = n,i[1],j
                # print(neighbors)
        n+=1    

            # x = t_loc[:][0] - i[0]
            # y = t_loc[:][1] - i[1]
            # math.sqrt(x**2+y**2)
            # min(i-t_loc)

    print(neighbors)

def dots():
    pass


t1 = track_circuits()
t2 = t_map_data()

# closest(t1,t2)

# s = t_map["features"][3000]


# tmap_nbr = 

# print(cur_circuit)
print(targets)