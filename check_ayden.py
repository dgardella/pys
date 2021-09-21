import requests
from xml.etree import ElementTree
url = 'https://pal-live.adyen.com/pal/servlet/soap/Recurring/listRecurringDetails'
data = '{"recurring": {"contract": "RECURRING"},"shopperReference": "pmoran@nubico.es/nubico","merchantAccount": "NubicoES"}'
response = requests.post(url, data=data,headers={"Content-Type": "application/json"},auth=('ws@Company.Yadican', 'bz=[437x/ncEFE3wdHHI@ik~r'))
print(response)
print(response.text)
