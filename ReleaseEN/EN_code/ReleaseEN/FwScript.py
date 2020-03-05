
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from supportFunc import *
import json
from grapInfo import * 


parameters = ReadJson()
parameters["FW_Name"] = ReadCodeFW()

webData = getWebInfo(CheckAndAddFwLastName(parameters["FW_Name"]),parameters["Username"],parameters["Password"])
parameters["FW_Name"] = checkFwLastName(parameters["FW_Name"])

CheckXLS()
MoveFile(parameters["FW_Name"])
RunWinRAR()

dataXLS = ReadXLS()
dataTXT = ReadTXT()

fileRAR = ReadRAR()
data = {
    'Username' : parameters['Username'],
    'Password' : parameters['Password'],
    'en_series' : webData["en_series"],
    'model_name2' : webData["model_name2"],
    'subject' : dataTXT[2].replace('AutoRun',webData["customer_code"]),
    'customer_code' : webData["customer_code"],
    'startDate' : SetTime(),
    'Context' : dataXLS[0],
    'Model_No' : dataXLS[1],
    'checksum' : dataTXT[3],
    'description' : webData["description"],
    'en_fw' : dataTXT[0],
    'partNum' : webData["partNum"],
    'rar_path' : {
        'bin' : fileRAR["bin"],
        'dat' : fileRAR["dat"],
        'FRF' : fileRAR["FRF"],
        'rar' : fileRAR["rar"]
    },
    'product_Category' : webData["product_Category"]
}



# 開始網頁腳本
driver = webdriver.Chrome()
driver.get("http://twhcp1w1/names.nsf?Login")


account = driver.find_element_by_name("Username")
password = driver.find_element_by_name("Password")

account.send_keys(data['Username'])
password.send_keys(data['Password'])

form = driver.find_element_by_name("_DominoForm")
form.submit()

time.sleep(1)

driver.switch_to.frame(driver.find_element_by_xpath("//frame[contains(@src,'/public/homepage.nsf/left?OpenForm')]"))
EN = driver.find_element_by_link_text("EN")
EN.click()

# 切回主網頁
driver.switch_to.parent_frame()

# frame right
driver.switch_to.frame(driver.find_element_by_xpath("//frame[contains(@src,'/public/homepage.nsf/a2?OpenFrameSet')]"))
driver.switch_to.frame(driver.find_element_by_xpath("//frame[contains(@src,'/public/homepage.nsf/a1?OpenFrameSet')]"))
driver.switch_to.frame(driver.find_element_by_xpath("//frame[contains(@src,'/public/homepage.nsf/ToDo?OpenForm')]"))


# Apply No:
# en_type不是絕對 name 要修改
FW = driver.find_element_by_name("en_type")
FW.click()
alert = driver.switch_to.alert
alert.accept()

#Product Catgory
productCatgary = driver.find_element_by_xpath('//input[@value="%s"]'%(data["product_Category"]))
productCatgary.click()

# Series
series = Select(driver.find_element_by_name("en_series"))
series.select_by_visible_text(data['en_series'])
alert = driver.switch_to.alert
alert.accept()

# Model Name
model_name2 = Select(driver.find_element_by_name("model_name2"))
model_name2.select_by_visible_text(data['model_name2'])
alert = driver.switch_to.alert
alert.accept()

# Subject 
subject = driver.find_element_by_name("subject")
subject.send_keys(data['subject'])

# Check Person

# Customer
customer_code = Select(driver.find_element_by_name("customer_code"))
customer_code.select_by_visible_text(data['customer_code'])

# Exp Date
nodefine = driver.find_element_by_name("nodefine")
nodefine.click()
driver.execute_script("document.forms[0].StartDate.value = '%s'"%(data['startDate']))
# startDate = driver.find_element_by_xpath('//input[@name="StartDate"]')
# startDate = driver.find_element_by_name("StartDate")
# startDate.value = "2020-02-10"


# Attachment
attachment = driver.find_element_by_id('upload1')
attachment.send_keys(data['rar_path']['bin'])
upload = driver.find_element_by_xpath('//input[@id="upload1"]/following-sibling::input[1]')
upload.click()

attachment = driver.find_element_by_id('upload1')
attachment.send_keys(data['rar_path']['dat'])
upload = driver.find_element_by_xpath('//input[@id="upload1"]/following-sibling::input[1]')
upload.click()

attachment = driver.find_element_by_id('upload1')
attachment.send_keys(data['rar_path']['FRF'])
upload = driver.find_element_by_xpath('//input[@id="upload1"]/following-sibling::input[1]')
upload.click()

# Issue To
# issueTo = driver.find_element_by_xpath('//input[@value="HCP"]')
# issueTo.click()

# Add Receiver

# Part No.
partNum = driver.find_element_by_name("f_part_no")
partNum.send_keys(data['partNum'])

# Description
description = driver.find_element_by_name("f_title")
description.send_keys(data['description'])

# PCB Main Board
pcbMainBoard = driver.find_element_by_name("PCB_Main_Board")
pcbMainBoard.send_keys("N/A")

# Audio Board
audioBoard = driver.find_element_by_name("Audio_Board")
audioBoard.send_keys("N/A")

# Vendor ID
vendorID = driver.find_element_by_name("vendor_id")
vendorID.send_keys("N/A")

# F/W Version
en_fw = driver.find_element_by_name("en_fw")
en_fw.send_keys(data['en_fw'])

# Servo
servo = driver.find_element_by_name("servo")
servo.send_keys("N/A")

# Aging Code
aging_code = driver.find_element_by_name("aging_code")
aging_code.send_keys("N/A")

# Product ID  (copy reguest form model name)
product_id = driver.find_element_by_name("product_id")
product_id.send_keys("N/A")

# Improved form F/W
improved_from = driver.find_element_by_name("improved_from")
improved_from.send_keys("N/A")

# Interface
interface = driver.find_element_by_name("interface")
interface.send_keys("N/A")

# Check sum
checksum = driver.find_element_by_name("checksum")
checksum.send_keys(data['checksum'])

# Model No.
Model_No = driver.find_element_by_name("Model_No")
Model_No.send_keys(data['Model_No'])

# OPC
opc = driver.find_element_by_name("opc")
opc.send_keys("N/A")

# Attachment FW SC
attachment = driver.find_element_by_id('upload5')
attachment.send_keys(data['rar_path']['rar'])
upload = driver.find_element_by_xpath('//input[@id="upload5"]/following-sibling::input[1]')
upload.click()

# Context
Context = driver.find_element_by_name("Context")
Context.send_keys(data['Context'])

# Generate Flow Node 提交表單
GFN = driver.find_element_by_xpath("//td[contains(text(),'Generate Flow Node')]")
GFN.click()
alert = driver.switch_to.alert
alert.accept()


























