import requests
import json
import urllib.request
import csv
import time
name = []
addresses = []
elevation = []
#-----------------------------------------------------------------------------------------------
#Bulk Entry- Uncomment the below lines if you plan on entering addresses in a bulk format
#ENTER FILE LOCATION HERE
filename = '<LOCATION + FILENAME.csv>'
with open(filename) as csvfile:
    address_reader = csv.reader(csvfile)
    for row in address_reader:
        addresses.append(row[0])
#-----------------------------------------------------------------------------------------------
#String Entry- Uncomment the below line if you plan on enterying addresses manually
#addresses = [<address 1>,<address 2>,<address 3>...<address n>]
#-----------------------------------------------------------------------------------------------
#geo_find will convert addresses to latitude longitude
def geo_find(address):
    time.sleep(2)
    geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    apikey = 'AIzaSyDnkqAjMB-TV3T5W5QhwOOi14s0y4tcZJY'
    params = {'sensor': 'false', 'address': address}
    r = requests.get(geocode_url, params=params)
    results = r.json()['results']
    location = results[0]['geometry']['location']
    lat = location['lat']
    lng = location['lng']
    return lat, lng
#-----------------------------------------------------------------------------------------------
#elevation_find will convert latitude longitude to elevation (elevations are in m)
def elevation_find(lat,lng):
    time.sleep(4)
    elevation_url = "https://maps.googleapis.com/maps/api/elevation/json"
    apikey = 'AIzaSyDnkqAjMB-TV3T5W5QhwOOi14s0y4tcZJY'
    a = requests.get(elevation_url+"?locations="+str(lat)+","+str(lng)+"&key="+apikey)
    results_all = a.json()['results']
    rs = results_all[0]
    results = (str(results_all[0]))
    null, results = results.split("'elevation':",1)
    time.sleep(5)
    if results.count(',')>0:
        results, null = results.split(",",1)
    else:
        results = results.replace("}",1)
    results = results.strip()
    return results
#-----------------------------------------------------------------------------------------------
#array_sorter will sort the array based off elevation (elevations are in m)
def array_sorter(arg1,arg2):
    data_list = arg1
    data_list_2 = arg2
    data_list_all = []
    for y in range(0,len(data_list),1):
        data_list_all.append(data_list[y])
    new_list = []
    new_list_2 = []
    while data_list:
        minimum = data_list[0]  # arbitrary number in list 
        for x in data_list: 
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)
    for y in range(0,len(new_list),1):
        for z in range(0,len(data_list_all),1):
            if new_list[y]==data_list_all[z]:
                s = data_list_2[z]
                new_list_2.append(s)
    return new_list, new_list_2
#-----------------------------------------------------------------------------------------------
#Compiling of Unsorted Addresses
for x in range(0,len(addresses),1):
    print(addresses[x])
    lat,long = geo_find(addresses[x])
    print(lat,long)
    elevate = elevation_find(lat,long)
    print(elevate)
    elevation.append(float(elevate))
    time.sleep(5)
#-----------------------------------------------------------------------------------------------
#Running the Sorted Function
elevation_sorted, addresses_sorted = array_sorter(elevation,addresses)
#-----------------------------------------------------------------------------------------------
#Printing out addresses and elevations (elevations are in m)
for y in range(0,len(elevation_sorted),1):
    print(addresses_sorted[y],elevation_sorted[y])
#-----------------------------------------------------------------------------------------------
#Compiling into csv
j = zip(addresses_sorted,elevation_sorted)
the_file_name_v2 = '<LOCATION OF FINAL READOUT>'
newfile= open(the_file_name_v2,'w')
for item in j:
    newfile.write("{},{}\n".format(*item))
newfile.close()
