import os
import glob
import xlrd 
import json


def read_excel():
    
    with xlrd.open_workbook(files_path_name[2]) as f:
        # print("xls file can open\n")
        data = {}
        arr_data = []
        
        sheet1 = f.sheets()[0]
        model_name = sheet1.cell_value(4,4) #grab model name
        arr_data.append(model_name)
        applyer = sheet1.cell_value(4,12)  #grab applyer
        arr_data.append(applyer)
        fw_name = sheet1.cell_value(16,9) + sheet1.cell_value(16,10) + sheet1.cell_value(16,11)#grab fw name
        arr_data.append(fw_name)

        sheet3 = f.sheets()[2]
        
        print("model name:\n", model_name)
        print("applyer:\n", applyer)
        print("vendor_fw_name:\n", fw_name)
        print("arr_data:\n", arr_data)
        # print(form_data[2])
        
        data = {
            'model_name': arr_data[0],
            'applyer': arr_data[1],
            'vendor_fw_name': arr_data[2],
        }
        
        # json_data = json.dumps(data)  
    return data, arr_data #,json_data# 

def getinfo():
    # os.system("start " + files_grab[0])
    # os.system("start " + files_grab[1])
    # os.system("start " + files_grab[2])    
    #all_param, data, arr_data = read_excel() #read files
    data, arr_data = read_excel()

    print("--------------------------------------------------------\n")
    with open('test22.txt', 'a+', encoding="utf-8") as f:
        f.write("test files:\n")
        for line in files_path_name:
            f.write("".join(line) + '\n')
        f.write("\n")    
        f.write("Request form info:\n")            
        for key, value in data.items():
            f.write(key + ':' + str(value))
            f.write("\n")
    return 1

if __name__ == '__main__':
    # datapath = "C:\\Users\\test\\Desktop\\readfile\\datafile\\.*"
    datapath = ".\datafile\*"
    types = ['*.txt', '*.dat', '*.xls'] ###grab file type###
    files_path_name = []

    for files in types: ###process###
        filename = glob.glob(datapath + files)
        # print(filename)
        files_path_name.extend(filename)
    print(files_path_name)   
    
    success = getinfo()
    if(success):
        print("\nprocess succed")
        os.system("pause")
    else: 
        print("\nprocess fail")