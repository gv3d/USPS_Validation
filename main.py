import pandas as pd
import requests


url = 'https://tools.usps.com/tools/app/ziplookup/zipByAddress'
temp = []

header_dict = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.7,fr-BE;q=0.3',
    'x-requested-with': 'XMLHttpRequest',
    'connection': 'keep-alive',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://tools.usps.com',
    'referer': 'https://tools.usps.com/zip-code-lookup.htm?byaddress',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
}

# створюємо pandas датафрейм 'df' з csv-файлу:
df = pd.read_csv("Input.csv", sep=';')

# кожний рядок значень з датафрейму 'df' підставляємо у форму USPS і перевіряємо на валідність:
for value in df.to_dict('records'):
    payload = {
        'companyName': value['Company'],
        'address1': value['Street'],
        'city': value['City'],
        'state': value['St'],
        'zip': value['ZIPCode'],
    }

    response = requests.post(url, headers=header_dict, data=payload)
    payload = response.json()

# наповнюємо пустий список 'temp' результатами перевірки:
    if payload.get('resultStatus', '') == 'SUCCESS':
        temp.append('Valid')
    else:
        temp.append('Invalid')


# створюємо колонку 'Validation' та додаємо її до датафрейму 'df':
new_df = pd.DataFrame({'Validation' : temp})
output = pd.concat([df, new_df], axis=1)
# записуємо вихідний csv-файл:
output.to_csv('Output.csv', sep=';', index=False)
print('Done!')
