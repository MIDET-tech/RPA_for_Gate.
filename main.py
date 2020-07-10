# main.py
import os
import csv
import time
from selenium import webdriver

#get username to specify an absolute path
username = os.getlogin()

#import mpdules
from module import module

driver = webdriver.Chrome()
module = module.modules(username,driver)

# Changing file format from Shift-JIS to utf-8
module.format_changer()

# Importing property data
print("Importing property data...")

data = open("data_utf-8.csv".format(username),'r',encoding="utf-8")
data_reader = csv.reader(data)
bukken_data = list(data_reader)

# Can change rows you want to input(default:bottom)
y = len(bukken_data) - 1

# Login Gate.
module.login()

time.sleep(3)

# Entering the property information
print("Entering the property information...")
module.property_information(y,bukken_data)

# Output GateMarketSurvey
print("Outputting GateMarketSurvey... ")
module.GateMarketSurvey(username)

handle_array_3 = driver.window_handles
driver.switch_to.window(handle_array_3[0])

time.sleep(7)

# Enter detailed information
print("Entering detailed information...")
module.detailed_information(y,bukken_data)

# Exporting assessment result
print("Exporting assessment result...")
module.assessment_result(y,bukken_data)

print("The assessment was completed successfully!")