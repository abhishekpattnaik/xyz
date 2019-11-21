players = {
        "Rohit":{"Run" : 200,
                "Wickets" : 10,
                "Average runs" : 43},
        "Dhoni":{"Run" : 200,
                "Wickets" : 10,
                "Average runs" : 43},
        "Shikhar":{"Run" : 200,
                "Wickets" : 10,
                "Average runs" : 43},
        'Gambhir':{"Run" : 200,
                "Wickets" : 10,
                "Average runs" : 43},
        'Shami':{"Run" : 200,
                "Wickets" : 10,
                "Average runs" : 43},
        'Kohli':{"Run" : 200,
                "Wickets" : 10,
                "Average runs" : 43},
        'Abhishek':{"Run" : 200,
                "Wickets" : 10,
                "Average runs" : 43}
}
lis=[]
for i in players.values():
        for j in i.values():
                lis.append(j)
print(lis)