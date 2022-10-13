from weather import *

jsonFile = "w.dat"
jsonDict = {}

while(True):
    print("*** TUFFY TITAN WEATHER LOGGER MAIN MENU ")
    print("1.Set data filename")
    print("2.Add weather data")
    print("3.Print daily report")
    print("4.Print historical report")
    print("9.Exit the program")
    select = int(input("Enter menu choice: "))
    if select == 1:
        jsonFile = input("Type in filename: ")
        jsonDict = read_data(jsonFile)
        print("File is readable")
    elif select == 2:
        date = input("Input date using YYYYMMDD format: ")
        time = input("Input time using hhmmss: ")
        temperature = int(input("Input temperature: "))
        humidity = int(input("Input humidity: "))
        rainfall = float(input("Input rainfall: "))
        jsonDict[date+time] = {'t':temperature, 'h':humidity, 'r':rainfall}
        write_data(jsonDict, jsonFile)
    elif select == 3:
        date = input("Input date: ")
        report_daily(jsonDict, date)
    elif select == 4:
        report_historical(jsonDict)
    elif select == 9:
     break


