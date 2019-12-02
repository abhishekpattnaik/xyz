import pandas as pd
dx = pd.read_csv('https://docs.google.com/spreadsheets/d/1G4sYrPtocF8eOoS4kEZtMQfMBTOc6luBu86Zm_vWiNA/edit#gid=1250910947')
print(dx[dx.star_rating>9])
dx.to_excel('AMN.xlsx',sheet_name='IMDB')
print('Successfully created')