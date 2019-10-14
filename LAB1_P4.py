import requests
from bs4 import BeautifulSoup
import csv

def rowgetDataText(tr, coltag='td'): # td (data) or th (header)
    cols = []
    for td in tr.find_all(coltag):
        cols.append(td.get_text(strip=True))
    return cols

def tableDataText(table):       
    rows = []
    trs = table.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append(rowgetDataText(tr, 'td')) # data row
    return rows#def search_spider(sea, lim):

page = requests.get("https://scikit-learn.org/stable/modules/clustering.html#clustering") 
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table', { 'class' : "colwidths-given docutils" })
list_table = tableDataText(table)
len(list_table)
#list_table[:2]
#import pandas as pd
#dftable = pd.DataFrame(list_table[1:], columns=list_table[0])
#print(dftable.head(4))
with open('Outputtalbe.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            for row in range (len(list_table)):
                writer.writerow(list_table[row])