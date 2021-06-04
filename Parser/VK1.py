#coding=utf-8
import vk
import sys

ids = str(sys.argv[1])
token = "9fedfe869fedfe869fedfe86da9f9a681d99fed9fedfe86ff6878bde6fbf0523510ed49"  # Сервисный ключ доступа
session = vk.Session(access_token=token)
api = vk.API(session, v='11.9.1')
person = api.users.get(user_ids=ids, fields='about, education, home_town, exports, interests, bdate')
print(person)
#'pavlovsemen'