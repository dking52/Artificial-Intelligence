#K-means clustering
#Random generated centroids and plot points
#Eval distance and assign cluster to centroid
#Count value for cluster/centroid assignment

import numpy as my_nump
import random
import math

#Variables
Centroid_Quantity = 3
pt_Quantity = 25
plot_coord = []
cluster_List = []
centroid_List = []

#Random points for x and y of plot_coord and centroids using numpy and permutation
my_nump.random.seed()

x = my_nump.random.permutation(pt_Quantity)
y = my_nump.random.permutation(pt_Quantity)
xPt_centroid = my_nump.random.permutation(pt_Quantity)
yPt_centroid = my_nump.random.permutation(pt_Quantity)

#For each item fed from pt_Quantity & Centroid_Quantity in given range of list, combine (x,y) and count value to new lists
for count in range(pt_Quantity):
    plot_coord.append([x[count], y[count], 1])
    
for count in range(Centroid_Quantity):
    centroid_List.append([xPt_centroid[count], yPt_centroid[count]])

#Get Distance between points using Euclidean Point Distance forumula and specific x or y coordinate
def p2p_Dist(pt1, pt2):
    x_dist = abs(pt1[0] - pt2[0])
    y_dist = abs(pt1[1] - pt2[1])
    point_Distance = math.sqrt(x_dist ** 2 + y_dist ** 2) # ** = ^
    return point_Distance

#Calculate centroid point_Distance using p2p_Dist function, from each point in list
def calc_Centroid(my_Point):
    point_Distance = []
    for count in range(Centroid_Quantity):
        point_Distance.append(p2p_Dist(my_Point, centroid_List[count]))
    return point_Distance.index(min(point_Distance))

#Each point assigned to appropriate centroid by count value
def centroid_Assign():
    for count in range(len(plot_coord)):
        plot_coord[count][2] = calc_Centroid(plot_coord[count])

#Organize points by assigned cluster [0,1,2]
def group():
    for count in range(Centroid_Quantity):
        cluster_List.append([])
    
    #Checking cluster # value against centroid value and appends to list if equal
    for count2 in range(len(plot_coord)):
        for count in range(Centroid_Quantity):
            if (plot_coord[count2][2] == count):
                cluster_List[count].append(plot_coord[count2])

#Update cluster means
def run_Kmeans():
    for count in range(Centroid_Quantity):
        X = 0
        Y = 0
        for my_Point in cluster_List[count]:
            X += my_Point[0]
            Y += my_Point[1]
        #Calculate centroid count by count of plot points / cluster value 
        centroid_List[count] = [X / len(cluster_List[count]), Y / len(cluster_List[count])]
        
#Print (x,y) of random points
def print_Point():
    for cluster in cluster_List:
        for my_Point in cluster:
            print(my_Point)

#Print (x,y) of random centroids
def print_Centroid():
    for my_Point in centroid_List:
        print(my_Point)

#Main
if __name__ == '__main__':   
    centroid_Assign()
    print ("\nStarting Centroid Location:")
    print_Centroid()
    group()
    run_Kmeans()

    print ("\nPoint (x,y) and Centroid Group:")
    print_Point()
    print ("\nOptimal Centroid Location:")
    print_Centroid()
    print ("\n")
    exit()