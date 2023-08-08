import pandas as pd

def get_unconventional_data(line, string, position):
    data = ""
    for c in string:
        if c == ',' or c == 'u': break
        if c == ':' or c == ' ': continue
        data = data + c
    return data

def check_data(line, dataType, position):
    unconventional = False
    data = dataType
    if dataType == 'price' or dataType == 'discount_price':
        data = 0.0
        unconventional = True
    elif dataType == 'early_access':
        data = True
        unconventional = True
    elif dataType == 'metascore':
        data = 1
        unconventional = True

    return unconventional, data

def get_data(line):
    data = []
    dataTemp = ''
    flagBegin = False
    flagProcess = False
    for i in range(len(line)):
        c = line[i]
        if c == 'u' and not flagBegin:
            flagBegin = True
        elif c == '\'' and flagBegin and not flagProcess:
            flagProcess = True
        elif c != '\'' and flagProcess:
            dataTemp = dataTemp + c
        elif c == '\'' and flagBegin and flagProcess:
            unconventional = False
            data.append(dataTemp)
            unconventional, dataTemp = check_data(line, dataTemp, i)
            if unconventional:
                data.append(dataTemp)
            dataTemp = ''
            flagBegin = False
            flagProcess = False
            unconventional = False
    return data

def add_to_df(df, string, parName):
    print("Some code")


parameters = ('publisher', 'genres', 'app_name', 'title',
              'url', 'release_date', 'tags',
              'discount_price','reviews_url', 'specs',
              'price', 'early_access', 'id', 'developer',
              'sentiment', 'metascore')

dataframe = []

f = open('Project\data\\raw\\steam_games.json', "r")

for i in range(2):
    row = []
    line = f.readline()
#for line in f:
    data = get_data(line)
    for i in data:
        if i in parameters:
            print("parameter: ", i)
        else:
            print("data: ", i)

f.close