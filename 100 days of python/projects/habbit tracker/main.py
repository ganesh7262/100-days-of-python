from datetime import datetime
import requests
TOKEN='peppovanish123'
USERNAME='peppovanish7262'
GRAPHID='peppotest123'

pixela_endpoint='https://pixe.la/v1/users'

user_params={
    "token":TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}


# response=requests.post(url=pixela_endpoint,json=user_params)

# print(response.json())

graph_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs'

header={
    'X-USER-TOKEN':'peppovanish123',
}

graph_params={
    'id':GRAPHID,
    'name':'cycling',
    'unit':'km',
    'type':'float',
    'color':'momiji'
}

# response=requests.post(url=graph_endpoint,json=graph_params,headers=header)
# print(response.json())


pixel_params={
    'date':str(datetime.today().date().strftime("%Y%m%d")),
    'quantity':input('Enter the Km: '),
}

pixel_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}'

response=requests.post(url=pixel_endpoint,json=pixel_params,headers=header)
print(response.json())

