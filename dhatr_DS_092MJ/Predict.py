!pip install haversine
#importing libraries for reading and calculating distance anf time
import haversine as hs
import numpy as np
import pandas as pd
import csv

def BuildEstimatedTravelTime():
  try:
    #input file is imported and stored in data1 data frame for reference
    data1=pd.read_csv('Input.csv')
    #print(data1) to verify

    #src is used to store source latitudes and longitudes 
    src=pd.read_csv('Input.csv',usecols=['Source_Lat','Source_Long'])

    #src_lat and src_long for source latitude and longitude respectively
    src_lat=pd.read_csv('Input.csv',usecols=['Source_Lat'])
    src_long=pd.read_csv('Input.csv',usecols=['Source_Long'])

    #dest_lat and dest_long for destination latitude and longitude respectively
    dest_lat=pd.read_csv('Input.csv',usecols=['Dest_Lat'])
    dest_long=pd.read_csv('Input.csv',usecols=['Dest_Long'])

    #length of src dataframe
    n=len(src.index)

    src01=pd.DataFrame()
    dest01=pd.DataFrame()

    for i in range(n):
    #latitides and longitudes for source and destination
      src01.append(src_lat[i],src_long[i])
      dest01.append(dest_lat[i],dest_long[i])


      #distance  are calculated between the latitudes and longitudes respectively
    from haversine import haversine_vector ,Unit
    dist=hs.haversine_vector(src01,dest01,Unit.KILOMETERS)
      #dist  vector elements are returned in kilometers
      #print(dist) for verification
    return dist
  except KeyError:
    return

#a vector for time is created to store the time taken to travel for distances
  #by numpy
lst=[]
time_dist=np.array(lst)
#dist_in_km=np.array([])

dist_in_km=np.array(BuildEstimatedTravelTime())

n=int(dist_in_km.size)
if(n==0):
  print()
else:  
  for i in range(n+1):
    try:
      time_dist[i].append(0) 
    except IndexError:
      break
  #distance/speed is used here
  #speed is 3*10^8 m/s

for i in range(n):
  try:
    time_dist[i]=dist_in_km[i]/(1/3*(10**5))
  except IndexError:
    break
  #time is printed and given as output
for i in range(len(time_dist)):
  print(time_dist[i])

  #to append time_dist into Input.csv file
with open('Input.csv','w') as output:
  writer=csv.writer(output, lineterminator='\n')
  for val in list(zip(*time_dist[::-1])):
    writer.writerow(val) 
