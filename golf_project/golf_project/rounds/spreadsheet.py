import pygsheets 


gc = pygsheets.authorize(service_account_file='/Users/narenas/git/golf-project/lgagolf-golf-project-ca104c4d33e5.json')

sh = gc.open('puntos_om')
wks = sh.sheet1

cell_matrix = wks.get_all_values(returnas='matrix')

print (cell_matrix)