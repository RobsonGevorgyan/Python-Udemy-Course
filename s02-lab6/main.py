import os
import urllib.request

data_dir = r" C:\Users\rgeworgjan\PycharmProjects\s02-lab6"

pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

path =[]
backslash = r"\ "
for i in range(len(pages)):

    filepath = data_dir + "\\" + pages[i-1]['url'] + ".html"
    path.append(filepath)

    urllib.request.urlretrieve(pages[i]['url'], path[i])

print(path)


