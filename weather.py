
import json
import calendar

def read_data(filename):
    try:
        file = open(filename)
        stuff = json.load(file)
        file.close()
        return stuff
    except FileNotFoundError:
        return {}
        
def write_data(data, filename):
     file = open(filename , 'w')
     json.dump(data, file)
     file.close()


def max_temperature(data, date):
    max_temp = 0
    for curr in data:
        if curr[0:8] == date:
            if max_temp <= data[curr]['t']:
                temp = data[curr]['t']
                if max_temp <= temp:
                    max_temp = temp
    return max_temp

def min_temperature(data, date):
    min_temp = 150
    for curr in data:
        if curr[0:8] == date:
            temp = data[curr]['t']
            if min_temp >= temp:
                 min_temp = temp
    return min_temp

def max_humidity(data, date):
    max_hum = 0
    for curr in data:
        if curr[0:8] == date:
            hum = data[curr]['h']
            if max_hum <= hum:
                 max_hum  = hum
    return max_hum

def min_humidity(data, date):
    min_hum = 1000
    for curr in data:
        if curr[0:8] == date:
            hum = data[curr]['h']
            if min_hum >= hum:
                 min_hum  = hum
    return min_hum

def tot_rain(data, date):
    sum = 0
    for curr in data:
        if curr[0:8] == date:
            sum += data[curr]['t']
    return sum

def report_daily(data, date):
    print("========================= DAILY REPORT ========================\n")
    print("Date" + "    " + "Time" + "    " + "Temperature" + "   " + "Humidity" + "   " + "Rainfall\n")
    
        
def report_historical(data):
     print("========================= DAILY REPORT ========================\n")
     print("Date" + "    " + "Minimum" + " " + "Maximum" + " " + "Minumum" + " " + "Maximum" + " " + "Total\n")
     print("Date" + "       " + "Temperature" + "      " + "Humidity" + "   " + "Rainfall\n")
    