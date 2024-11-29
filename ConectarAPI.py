import requests
from InserirMegasena import *

url = "https://loteriascaixa-api.herokuapp.com/api/megasena"

response = requests.get(url)


if response.status_code == 200:
    concurso = response.json()
    for i in concurso:
        #print(i)
        if i['data'].endswith("2024"):
            concurso = i['concurso']
            data = i['data']
            dezenas1 = i['dezenas'][0]
            dezenas2 = i['dezenas'][1]
            dezenas3 = i['dezenas'][2]
            dezenas4 = i['dezenas'][3]
            dezenas5 = i['dezenas'][4]
            dezenas6 = i['dezenas'][5]
            #print(concurso, data, dezenas1, dezenas2, dezenas3, dezenas4, dezenas5, dezenas6)
            inserirbanco("megasena", data, concurso, dezenas1, dezenas2, dezenas3, dezenas4, dezenas5, dezenas6)
 
    # workbook =openpyxl.Workbook()
    # sheet = workbook.active
    # sheet.title = "Dados da API"
    # sheet.append(["Número do Concurso", "Data do Concurso", "Números Sorteados"])

    # for i in concurso:
    #     sheet.append([i["numero"], i["data"], i["numeros"]])

    # workbook.save("dados_api.xlsx")
    # print("Dados salvos no arquivo dados_api.xlsx")

else:
    print(f"Erro ao obter os dados da API, Status code: {response.status_code}")