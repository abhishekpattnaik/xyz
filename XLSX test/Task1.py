import pandas as pd 
import xlsxwriter
xlObjext = pd.read_excel('trafficking.xlsx')
rowNo = 0
main_dict = {}
for adName in xlObjext.advertiser_name:
    rowObj=xlObjext.loc[rowNo]
    rowNo+=1
    if adName in main_dict.keys():
        if rowObj.brand_name in main_dict[adName].keys():
            if rowObj.show not in main_dict[adName][rowObj.brand_name]:
                main_dict[adName][rowObj.brand_name].append(rowObj.show)
        else:
            main_dict[adName][rowObj.brand_name]=[rowObj.show]
    else:
        main_dict[adName]={rowObj.brand_name:[rowObj.show]}
workbook = xlsxwriter.Workbook("Assignment1.xlsx")
worksheet = workbook.add_worksheet()
rowNo=1
worksheet.write(0,0,'Advertiser Name',)
worksheet.write(0,1,'Brand Name')
worksheet.write(0,2,'Show')
for advertiser_name in main_dict.keys():
    for brand_name in main_dict[advertiser_name].keys():
        for show_name in main_dict[advertiser_name][brand_name]:
            worksheet.write(rowNo,0,advertiser_name)
            worksheet.write(rowNo,1,brand_name)
            worksheet.write(rowNo,2,show_name)
            rowNo+=1
workbook.close()
# print(pd.DataFrame(main_dict))