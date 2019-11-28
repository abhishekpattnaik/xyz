import pandas as pd 
# import pdb;pdb.set_trace() 
x1 = pd.read_excel('trafficking.xlsx')
c = 0
D = {}
for i in x1.advertiser_name:
    x2=x1.loc[c]
    c=c+1
    if i in D.keys():
        if x2.brand_name in D[i].keys():
            D[i][x2.brand_name].append(x2.show)
        else:
            D[i][x2.brand_name]=[x2.show]
    else:
        D[i]={x2.brand_name:[x2.show]}
x3 = pd.DataFrame(D)
x3.to_csv('testing1.csv')
for i in D.keys():
    for j in D[i].keys():
        for k in D[i][j]:
            print(i,'(Advertiser Name)\t',j,'(Brand Name)\t',k,'(Shows)')
print('Program ends here \n thank you')