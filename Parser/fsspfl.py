

import requests
import json
import time

token = "igaAOGpeDc5L"
firstname = input('Введите имя')
lastname = input('Введите фамилию')
region = input('Введите регион')
birthdate = input('Введите дату рождения дд.мм.гггг')

get_params = {'token': 'igaAOGpeDc5L', 'region': region, 'firstname': firstname, 'lastname': lastname, 'birthdate': birthdate}
response = requests.get('https://api-ip.fssp.gov.ru/api/v1.0/search/physical', params=get_params)
todos = json.loads(response.text)
values = list(todos.values())
# print(values[3])
val = list(values[3].values())
print(val[0])
v = str(val[0])
status = requests.get('https://api-ip.fssp.gov.ru/api/v1.0/status', params={'token': 'igaAOGpeDc5L', 'task': v})
stat = json.loads(status.text)
sta = list(stat.values())
st = list(sta[3].values())
s = int(st[0])
while s != 0:
    time.sleep(3)
    status = requests.get('https://api-ip.fssp.gov.ru/api/v1.0/status', params={'token': 'igaAOGpeDc5L', 'task': v})
    stat = json.loads(status.text)
    sta = list(stat.values())
    st = list(sta[3].values())
    s = int(st[0])
result = requests.get('https://api-ip.fssp.gov.ru/api/v1.0/result', params={'token': 'igaAOGpeDc5L', 'task': v})
print(result.json())

