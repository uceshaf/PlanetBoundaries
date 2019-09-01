#!/usr/bin/env python

""" Searches, Acitvates and gets the download links of Planet Data
PLANET_API_KEY is required to submit the request and can be changed
AOI coordinates in proper format may be downloaded from geojson.io
Dates can be changed to get the results


@returns: a file containing the download links of the activated images in the search query

Author: Syed Roshaan Ali Shah
"""

import os
# The requests library needs to be installed to run this
# On mac you may also need to uncomment the below lines if there is an error
#os.system('pip install tornado --user')
os.system('pip install requests --user')
import json
import requests
from requests.auth import HTTPBasicAuth
# The time module is needed to sleep timer before making calls to check activation of assets
import time




# ----------------------------------------------------------------------------------------- #
# ***************************************************************************************** #

# "Please replace your API Key below inside the quotes"
#Jan
PLANET_API_KEY = 'b003bbc8301e44f6b2dd2e408cd03b6a'

#mine
PLANET_API_KEY = 'ae0962e81766412693fbbd6d03c12a03'

# Ibrahim
PLANET_API_KEY = '7b2ce2acc5aa408bac2aceb89fcde297'

#Steve
PLANET_API_KEY = 'a1b456092b68452f9b924af2dcd9ffde'

#Mehmoud
#PLANET_API_KEY = ''



# ***************************************************************************************** #
# ----------------------------------------------------------------------------------------- #





##---------------------------------------------------------------------------------##

#item_type = "SkySatScene"

item_type = "PSScene4Band"

##-----------------------------FILTERS DEFINITION--------------------------------------##

# The Simplified AOI 

geojson_geometry = {
    "type":"Polygon",
    "coordinates":
    [
        [
            [10.547,57.2271],[10.5166,57.391400000000004],
[10.546000000000001,57.450700000000005],[10.448500000000001,57.534200000000006],[10.4519,57.6297],[10.6212,57.752],
[10.3239,57.6364],[10.1235,57.588800000000006],[9.9358,57.583600000000004],[9.7948,57.4761],[9.6416,57.3089],[9.5291,57.219300000000004],
[9.276,57.1441],[8.961500000000001,57.1539],[8.7418,57.098800000000004],[8.5882,57.118],[8.3627,56.961000000000006],[8.2279,56.781000000000006],[8.355500000000001,56.677600000000005],[8.4322,56.6351],[8.3062,56.5812],[8.2835,56.5856],[8.186200000000001,56.633700000000005],[8.1227,56.5549],[8.129800000000001,56.330000000000005],[8.1058,56.108000000000004],
[8.3033,56.057700000000004],[8.3744,55.9455],[8.3568,55.892],[8.184800000000001,55.868300000000005],[8.1506,55.6901],
[8.0782,55.556900000000006],[8.2568,55.5223],[8.450000000000001,55.4546],[8.6209,55.4284],[8.683900000000001,55.164],[8.634,55.0321],
[8.636700000000001,54.9134],[8.7279,54.892700000000005],[8.9482,54.9025],[9.240300000000001,54.849900000000005],[9.3421,54.8036],
[9.6052,54.9102],[9.7188,54.9035],[9.738100000000001,54.987300000000005],[9.63,55.0103],[9.491100000000001,55.119400000000006],
[9.5961,55.194100000000006],[9.693800000000001,55.1952],[9.5929,55.417],[9.639100000000001,55.5093],[9.6553,55.5172],[9.656500000000001,55.5167],
[9.7017,55.4947],[9.707600000000001,55.4919],[9.8093,55.4433],[9.8741,55.3509],[9.885100000000001,55.2594],[10.0226,55.181200000000004],
[10.1125,55.1897],[10.1865,55.078300000000006],[10.5108,55.0268],[10.743500000000001,55.0688],[10.8222,55.3081],[10.686,55.4384],
[10.7474,55.476800000000004],[10.660300000000001,55.557300000000005],[10.936300000000001,55.6633],[11.1141,55.632600000000004],
[11.2028,55.4506],[11.2043,55.383700000000005],[11.123700000000001,55.337500000000006],[11.226,55.2911],[11.309800000000001,55.194700000000005],[11.4334,55.2194],[11.7166,55.1561],[11.742,55.094],[11.896500000000001,54.9947],[12.053,54.962700000000005],[12.1707,55.004400000000004],[12.086,55.122600000000006],[12.157300000000001,55.212700000000005],[12.3574,55.2378],[12.4509,55.2824],[12.3651,55.3971],[12.2155,55.4277],[12.2445,55.546400000000006],[12.3835,55.612100000000005],[12.49,55.6004],[12.616000000000001,55.720600000000005],[12.5174,55.920100000000005],[12.617600000000001,56.038900000000005],[12.4989,56.0912],
[12.3092,56.1291],[12.1826,56.109300000000005],[11.8522,55.9748],[11.9601,55.8519],[11.878,55.814],[11.839,55.688100000000006],[11.7492,55.7391],[11.6689,55.9136],[11.538,55.9523],[11.4925,55.847],[11.377,55.822900000000004],[11.348700000000001,55.757200000000005],[11.175500000000001,55.7546],[11.092600000000001,55.676700000000004],[11.0982,55.6653],[10.936300000000001,55.671200000000006],[10.6537,55.563500000000005],[10.5997,55.613400000000006],[10.6242,55.487100000000005],[10.4284,55.441700000000004],[10.506300000000001,55.5445],[10.3254,55.6195],[10.0381,55.5574],[9.9452,55.5135],[9.8384,55.553200000000004],[9.836,55.554500000000004],[9.797600000000001,55.586600000000004],[10.0289,55.6995],[10.073500000000001,55.8844],[10.193,55.8371],[10.255700000000001,55.9117],[10.2711,56.048100000000005],[10.2138,56.158],[10.449200000000001,
56.291700000000006],[10.451400000000001,56.1817],[10.639700000000001,56.1747],[10.914100000000001,56.3431],[10.9501,56.4564],[10.836300000000001,56.5308],[10.5303,56.5127],[10.3468,56.576800000000006],[10.363100000000001,56.6617],[10.2765,56.801],[10.265500000000001,56.881800000000005],[10.2657,56.881800000000005],[10.2644,56.9072],[10.345,57.0078],[10.3504,57.0086],[10.363000000000001,57.030300000000004],[10.3696,57.0386],[10.3683,57.039500000000004],[10.4456,57.1734],[10.547,57.2271]],[[9.1323,57.040000000000006],[9.2272,56.9932],[9.242600000000001,56.962300000000006],[9.1797,56.9198],[9.1704,56.809400000000004],[9.222000000000001,56.716],[9.324900000000001,56.661500000000004],[9.163400000000001,56.6236],[9.1745,56.7119],
[9.067,56.802600000000005],[8.8671,56.7609],[8.7269,56.6233],[8.7315,56.4782],[8.6483,56.4671],[8.6157,56.4851],[8.628,56.5414],[8.6007,56.6794],[8.5507,56.702000000000005],[8.5481,56.7004],[8.469100000000001,56.7794],[8.632900000000001,56.8644],[8.6706,56.9523],[8.757,56.9457],[8.981300000000001,57.016400000000004],[9.1323,57.040000000000006]
]
]
}


# get images that overlap with our AOI 
geometry_filter = {
  "type": "GeometryFilter",
  "field_name": "geometry",
  "config": geojson_geometry
}

# get images acquired within a date range

##
##date_range_filter = {"type": "OrFilter",
##                     "config":
##                     [{
##  "type": "DateRangeFilter",
##  "field_name": "acquired",
##  "config":
##  {
##    "gte": "2018-10-11T00:00:00.000Z",
##    "lte": "2018-10-12T00:00:00.000Z"}},            
##    {"type": "DateRangeFilter",
##  "field_name": "acquired",
##  "config": {
##    "gte": "2018-04-20T00:00:00.000Z",
##    "lte": "2018-04-21T00:00:00.000Z"
##  }}]}
##


date_range_filter = {"type": "OrFilter",
                     "config":
                     [{
  "type": "DateRangeFilter",
  "field_name": "acquired",
  "config":
  {
    "gte": "2018-10-11T00:00:00.000Z",
    "lte": "2018-10-11T00:00:00.000Z"}},            
    {"type": "DateRangeFilter",
  "field_name": "acquired",
  "config": {
    "gte": "2018-04-20T00:00:00.000Z",
    "lte": "2018-04-21T00:00:00.000Z"
  }}]}

100231

# only get images which have <3% cloud coverage
cloud_cover_filter = {
  "type": "RangeFilter",
  "field_name": "cloud_cover",
  "config": {
    "gte":0,
    "lte": 0.03
  }
}


cloud_cover_filter = {
  "type": "RangeFilter",
  "field_name": "cloud_cover",
  "config": {
    "gte":0,
    "lte": 0.001
  }
}


# combine our geo, date, cloud filters
combined_filter = {
  "type": "AndFilter",
  "config": [geometry_filter, date_range_filter, cloud_cover_filter]
}


##-----------------------------FILTERS DEFINITION END--------------------------------------##




#starting a session as the results are more
session = requests.Session()
session.auth = (PLANET_API_KEY, '')



# API request object
search_request = {
  "name": "search_requestPScape",
  "item_types": [item_type], 
  "filter": combined_filter
}
print("Searching for images within the filters")



search_result = \
  session.post(
    'https://api.planet.com/data/v1/searches/',
    auth=HTTPBasicAuth(PLANET_API_KEY, ''),
    json=search_request)

#print(json.dumps(search_result.json(), indent=1))

# after you create a search, save the id. This is what is needed
# to execute the search.
saved_search_id = search_result.json()["id"]




# What we want to do with each page of search results
# in this case, just print out each id
image_ids=[]
def handle_page(page):
    for item in page["features"]:
        image_ids.append(item["id"])
        #print(item["id"])

# How to Paginate:
# 1) Request a page of search results
# 2) do something with the page of results
# 3) if there is more data, recurse and call this method on the next page.
def fetch_page(search_url):
    page = session.get(search_url).json()
    handle_page(page)
    next_url = page["_links"].get("_next")
    if next_url:
        fetch_page(next_url)

first_page = \
    ("https://api.planet.com/data/v1/searches/{}" +
        "/results?_page_size={}").format(saved_search_id, 250)
# kick off the pagination
fetch_page(first_page)






# extract image IDs only
print(image_ids)
print(len(image_ids))






# ---------------------- Starting Process of Actiavtions -------------------


status_dict = {}
links_dict = {}
for idx in image_ids:
    idx_url = 'https://api.planet.com/data/v1/item-types/{}/items/{}/assets'.format(item_type, idx)
    #print("\n Checking URL ......................................... ")
    #print(idx_url)
    # Returns JSON metadata for assets in this ID. Learn more: planet.com/docs/reference/data-api/items-assets/#asset
    result = requests.get(
        idx_url,
        auth=HTTPBasicAuth(PLANET_API_KEY, '')
        )
    # Checking for retrying rate limit error
    if result.status_code == 429:
        raise Exception("rate limit error")
    #print("Printing Results of idx: ")
    #print(result.json())
    # List of asset types available for this particular satellite image
    #print("List of asset types available for this particular satellite image: ")
    #print(result.json().keys())
    
    #Getting imp info from result
    permissions = result.json()[u"analytic"]["_permissions"]
    links = result.json()[u"analytic"]["_links"]
    self_link = links["_self"]
    activation_link = links["activate"]
    status = result.json()['analytic']['status']
    print(idx,' : ',status)
    #print('The status of this resource is: '+str(status))
    if 'download' in permissions:
        #print("You have permission to download this resource")
        status_dict.update({idx:status})
        links_dict.update({idx: (self_link,activation_link)})
        if status != 'active':
            activate_result = requests.get(
                activation_link,
                auth=HTTPBasicAuth(PLANET_API_KEY, '')
                )
            #Check if it's activating or not
##            activation_status_result = \
##              requests.get(
##                self_link,
##                auth=HTTPBasicAuth(PLANET_API_KEY, '')
##                )
##            status_idx = activation_status_result.json()["status"]
##            status_dict.update({idx:status_idx})
##        else:
##            status_dict.update({idx:'active'})
    else:
        print("You do not have permission to download this resources")
        continue
    

print(status_dict)




# ----------------------- Checking Activations -------------------------
print("Waiting for 2 minutes to check again for activate status of the images")
#time.sleep(120)
print("\n\n ---------------------------------------------------------")

download_links={} 
while ('activating' in status_dict.values()) or 'inactive' in status_dict.values():
    # .......................
    print("\n Waiting for 1-minute to check again for activate status of the images")
    time.sleep(30)
    # .......................
    print("\n The current activation status dictionary of the assests is: ")
    print(status_dict)
    
    print("\n\nCheking again for active status...")
    for idx, link in links_dict.items():
        self_link=link[0]
        # Checking the status of the activations
        activation_status_result = \
                  requests.get(
                    self_link,
                    auth=HTTPBasicAuth(PLANET_API_KEY, '')
                    )
        
        status = activation_status_result.json()["status"]
        status_dict[idx]=status
        print(idx,' : ',status)
        activation_link=link[1]
        
        if (status != 'active') and (status != 'activating'):
            print("Still not active or activating, this one")
            # activating the inactive ones
            activate_result = requests.get(
                    activation_link,
                    auth=HTTPBasicAuth(PLANET_API_KEY, '')
                    )
            # Checking for retrying rate limit error
            if result.status_code == 429:
                raise Exception("rate limit error")
        #if status == 'active':
         #   download_links.update({idx:activation_status_result.json()["location"]})
             # WAIT for checking again





print("Fetching the download links now \n\n\n")
for idx, link in links_dict.items():
    #WE need to change the self_link accordingly
    self_link=links_dict[idx][0]
    activation_status_result = requests.get(
                    self_link,
                    auth=HTTPBasicAuth(PLANET_API_KEY, '')
                    )
    status = activation_status_result.json()["status"]
    #print(activation_status_result.json())
    #print(activation_status_result.json()["location"])
    if status == 'active':
        dlink = activation_status_result.json()["location"]
        os.system('curl -L '+str(dlink)+' > d:\Pdownloads\\'+str(idx)+'_3B_AnalyticMS.tif \n')
        download_links.update({idx:activation_status_result.json()["location"]})
            
    

    
#print("\n The final activation status dictionary of the assests is: ")
#print(status_dict)
#print(download_links)

with open('PlanetScape_DownLinks.csv','w+') as output:
    for key, value in download_links.items():
        output.write(str(key)+','+str(value)+'\n')
        
# The csv file DownLinks.csv is stored in the folder where the script is.
with open('PlanetScape_CurlCommands.bat','w+') as output:
    for key, value in download_links.items():
        output.write('curl -L '+ str(value)+ ' > d:\Pdownloads\\'+str(key)+'_3B_AnalyticMS.tif \n')



# The output files are in the scripts folder

