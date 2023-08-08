parameters = ('publisher', 'genres', 'app_name', 'title',
              'url', 'release_date', 'tags',
              'discount_price','reviews_url', 'specs',
              'price', 'early_access', 'id', 'developer',
              'sentiment', 'metascore')

stringParametersList = []

def checkIfParameter(line, pos, length):
    stringPosParameter = ""
    actParameter = False
    new_i = length + 1
    if pos == length:
        actParameter = True
    else: 
        for j in range(pos, length):
            stringPosParameter = stringPosParameter + line[j]
            if stringPosParameter in stringParametersList:
                actParameter = True
            if (line[j - 1] == "'" and line[j] == ":"):
                break
            elif (line[j] == "u" and line[j + 1] == "'"):
                stringPosParameter = "u"
                new_i = j
    return actParameter, new_i

def get_data(line, pos, length):
    stringData = ""
    posParameter = False
    actParameter = False
    new_i = 0
    for i in range(pos, length):
        posParameter = line[i] == "u" and line[i + 1] == "'"
        if posParameter:
            actParameter, new_i = checkIfParameter(line, i, length)
            posParameter = False
        if actParameter:
            for k in range(i, new_i):
                stringData = stringData + line[k]
            break
    return stringData, new_i

def get_parameter(line):
    data = []
    dataTemp = ""
    flagBegin = False
    i = 0
    length = len(line)
    while i < length:
        c = line[i]
        if line[i] == "u" and line[i + 1] == "'":
            flagBegin = True
            dataTemp = ""
        if flagBegin:
            dataTemp = dataTemp + c
        if dataTemp in stringParametersList:
            print("Se ha encontrado el parametro " + dataTemp)
            dataTemp, i = get_data(line, i, length)
            data.append(dataTemp)
            flagBegin = False
        i = i + 1
    return data

for i in parameters:
    stringParametersList.append("u'" + i + "':")
print(stringParametersList)

possible_values = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

f = open('Project\data\\raw\\steam_games.json', "r")
word = ""
for i in range(2):
    line = f.readline()
    data = get_parameter(line)
    print(data)
    print(len(data))
f.close()
