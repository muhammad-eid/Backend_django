import requests
from encrypt import encrypt_
activate_url = 'http://0.0.0.0:8000/api/activate'

data = {
    'key': 'key',
    'type': 'type',
    'duration': 'duration',
    'user_name': 'user_name',
    'uuid': 'uuid',
    'hddid': 'hddid',
    'mac_address': 'mac_address',
    'os_version': 'os_version',
    'sw_version': 'sw_version',
}
print(encrypt_(data))
response = requests.post(activate_url, json={'data': str(encrypt_(data))})
# print(encrypt.decrypt_(page.content))
print(response.json())