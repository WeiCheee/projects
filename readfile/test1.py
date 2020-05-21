import win32com.client as win32
import pandas as pd


def tansfer_table(path, num):
    df = pd.read_excel(path, index_col=False, nrows = num,  usecols = "A:L")
    html_table = df.to_html()

    print(html_table)

    outlook = win32.gencache.EnsureDispatch('Outlook.Application')
    mail_item = outlook.CreateItem(0)
    mail_item.To = 'Charles.Hsu@ssstc.com'
    print(path)
    #  modify the mail body as per need

    # mail_item.Attachments.Add(Source=path)
    # body = "<h1>Dear ABC</h1>This is the Table <br><br>   "+html_table+"   <br><br> this is image <br><br><img src=ownload.png><br><br>Thanks"
    body = html_table
    mail_item.HTMLBody = (body)
    mail_item.Send()

    return 1

if __name__ == '__main__':
    number = 8
    path = "C:\\Users\\test\\Desktop\\projects\\readfile\\datafile\\CV8_FW_Relation.xlsm"
    success = tansfer_table(path, number)
    if(success):
        print("\nprocess succed")
        # os.system("pause")
    else: 
        print("\nprocess fail")