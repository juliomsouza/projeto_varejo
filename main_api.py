import requests
from requests.auth import HTTPBasicAuth
import json
from pprint import pprint

# endpoint: http://localhost:6017/api/millenium/$help?


headers ={'Content-type': 'application/json'}
#response = requests.get("http://177.85.161.13:6017/api/millenium/clientes/busca?cliente=4", auth = HTTPBasicAuth('integracao', '5G34rf9'), headers=headers, timeout=3) 
response = requests.get("http://localhost:6017/api/millenium/clientes/busca?cliente=51500", auth = HTTPBasicAuth('julio souza', 'dimaro@1205'), headers=headers, timeout=3) 
#response = requests.get("http://localhost:6017/api/millenium/clientes/procura?cod_cliente={4}", auth = HTTPBasicAuth('julio souza', 'dimaro@1205'), headers=headers,timeout=3) 
#response = requests.get("http://localhost:6017/api/millenium/movimentacao/movimentacaosimples?evento='ENTRADA CONSERTO ANTIX CASA'&$format=json", auth = HTTPBasicAuth('julio souza', 'dimaro@1205'), headers=headers,timeout=3) 
print(response.status_code)

data = response.json()


pprint(data)


