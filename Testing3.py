import pandas as pd 
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
x3 = pd.DataFrame(main_dict,columns=['Advertiser Name','Brand Name','Show'])

D={}
ad=[]
bn=[]
sn=[]
for i in main_dict.keys():
    for j in main_dict[i].keys():
        for k in main_dict[i][j]:
            ad.append(i)
            bn.append(j)
            sn.append(k)
D['advertiser_name']=ad
D['brand_name']=bn
D['show_name']=sn      
xx = pd.DataFrame(D)
print(x3)