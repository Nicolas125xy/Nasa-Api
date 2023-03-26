import requests
# chave de API 
api_key = 'Key Api'
dates = input('Data em ANO-MÊS-DATA || ex:(2000-03-04): ')

# link da API 
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={dates}'

response = requests.get(url)

data = response.json()

print('Data:', data['date'])
print('Título:', data['title'])
print('URL: ', data['url'])
