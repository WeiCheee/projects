from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from supportFunc import *
import json
import sys
import os

def getWebInfo(NewFWName,Username,Password):

    # 指定下載路徑
    now_dir = os.getcwd()
    downloadPath = "%s\Data_Put_Here"%(now_dir)
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups':0,'download.default_directory':downloadPath}
    options.add_experimental_option('prefs',prefs)


    # 開始網頁腳本
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("http://twhcp1w1/names.nsf?Login")


    account = driver.find_element_by_name("Username")
    password = driver.find_element_by_name("Password")

    account.send_keys(Username)
    password.send_keys(Password)

    form = driver.find_element_by_name("_DominoForm")
    form.submit()

    time.sleep(1)

    driver.switch_to.frame(driver.find_element_by_xpath("//frame[contains(@src,'/public/homepage.nsf/left?OpenForm')]"))

    all_document = driver.find_element_by_xpath("//font[text()='All Document']")
    all_document.click()
    time.sleep(1)


    FW = driver.find_element_by_xpath("//a[contains(@href,'/public/app_FWR.nsf/V_all?OpenForm&login')]")
    FW.click()


    # 切回主網頁
    driver.switch_to.parent_frame()

    # frame right
    driver.switch_to.frame(driver.find_element_by_xpath("//frame[contains(@src,'/public/homepage.nsf/a2?OpenFrameSet')]"))
    driver.switch_to.frame(driver.find_element_by_xpath("//frame[contains(@src,'/public/homepage.nsf/a1?OpenFrameSet')]"))
    driver.switch_to.frame(driver.find_element_by_xpath("//frame[contains(@src,'/public/homepage.nsf/ToDo?OpenForm')]"))



    # Todo --> 查找總頁數 (寫死的可以改)
    for i in range(1,200):
        try:
            page = driver.find_element_by_xpath("//font[text()='PageNo:1/%s']"%(i))
            all_page_num = i
        except:
            continue

    for i in range(0,all_page_num):
        try:
            FW_Name = driver.find_element_by_link_text(NewFWName)
            FW_Name.click()
            break
        except:
            Page_Down = driver.find_element_by_xpath("//td[text()='Page Down']")
            Page_Down.click()

    # 確認是否有找到FW
    try:
        FW_Name
    except:
        print('Could not find FW name, please check your FW name')
        sys.exit()


    Product_Category = driver.find_element_by_xpath("//td[text()='Series']/preceding-sibling::td[1]").text
    Series = driver.find_element_by_xpath("//td[text()='Series']/following-sibling::td[1]").text

    Model_Name = driver.find_element_by_xpath("//td[text()='Model Name']/following-sibling::td[1]").text
    Customer = driver.find_element_by_xpath("//td[text()='Customer']/following-sibling::td[1]").text

    Version_Type = driver.find_element_by_xpath("//td[text()='Version Type']/following-sibling::td[1]").text
    New_FW_Name = driver.find_element_by_xpath("//td[text()='New F/W Name']/following-sibling::td[1]").text



    # /../tr/td/following-sibling::td[1]

    partNum = driver.find_element_by_xpath("//td[text()='Part No']/parent::tr/following-sibling::tr[1]/child::td").text
    description = driver.find_element_by_xpath("//td[text()='Part No']/parent::tr/following-sibling::tr[1]/child::td/following-sibling::td[1]").text

    time.sleep(1)

    # 檢查是哪個容量的
    if(Model_Name.find("128") != -1):
        stroge = "128"
    elif(Model_Name.find("256") != -1):
        stroge = "256"
    elif(Model_Name.find("512") != -1):
        stroge = "512"
    elif(Model_Name.find("1024") != -1):
        stroge = "1024"


    # 判斷容量
    a_href = driver.find_element_by_xpath("//td[text()='Cut in Bom(Y/N)']/parent::tr/parent::tbody/parent::table/following-sibling::table[1]/child::tbody/child::tr/following-sibling::tr[1]/child::td/child::table/child::tbody/child::tr/child::td/following-sibling::td[1]/child::a")
    a_href_str = a_href.text
    if(a_href_str.find(stroge) == -1):
        test_num=0
        i=1
        while(True):
            try:
                a_href = driver.find_element_by_xpath("//td[text()='Cut in Bom(Y/N)']/parent::tr/parent::tbody/parent::table/following-sibling::table[1]/child::tbody/child::tr/following-sibling::tr[1]/child::td/child::table/child::tbody/child::tr/following-sibling::tr[%s]/child::td/following-sibling::td[1]/child::a"%(i))
                a_href_str = a_href.text
                if(a_href_str.find(stroge) != -1):
                    break
                else:
                    i = i + 1
            except:
                break

    # a_href = driver.find_element_by_xpath("//td[text()='Cut in Bom(Y/N)']/parent::tr/parent::tbody/parent::table/following-sibling::table[1]/child::tbody/child::tr/following-sibling::tr[1]/child::td/child::table/child::tbody/child::tr/child::td/following-sibling::td[1]/child::a")
    a_href.click()

    data = {
        "partNum" : partNum,
        "model_name2" : Model_Name,
        "customer_code" : Customer,
        "en_series" : Series,
        "description" : description,
        "product_Category" : Product_Category,
    }
    return data