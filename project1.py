import csv

AIR_QUALITY_FILE = "air_quality.csv"
UHF_FILE = "uhf.csv"
list_of_data = []


UFH_to_measurements = {}
date_to_measurements = {}
zip_to_geo_ID = {}
borough_to_geo_ID = {}


#need utf-8-sig to read the file correctly
with open(AIR_QUALITY_FILE, encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    for row in reader:
        list_of_data.append(tuple(row))
        
        
def UFH_to_measurements_func():
    for tup in list_of_data:
        if(tup[0] not in UFH_to_measurements):
            UFH_to_measurements[tup[0]] = []
        UFH_to_measurements[tup[0]].append(tup)

def date_to_measurements_func():
    for tup in list_of_data:
        if(tup[0] not in date_to_measurements):
            date_to_measurements[tup[0]] = []
        date_to_measurements[tup[0]].append(tup)
        
def zip_to_geo_ID_func():
    info_file = open(UHF_FILE, "r")
    newLine = info_file.readline()
    while(newLine != ''):
        temp_list = newLine.split(",")
        for i in range(3,len(temp_list)):
            current_zip = temp_list[i].strip()
            geo_ID = temp_list[2].strip()
            print(current_zip)
            if(current_zip not in zip_to_geo_ID):
                zip_to_geo_ID[current_zip] = []
            zip_to_geo_ID[current_zip].append(geo_ID)
        newLine = info_file.readline()
#def borough_to_geo_ID_func():
    #for


zip_to_geo_ID_func()
print(zip_to_geo_ID)
