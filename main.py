import requests

import webbrowser

##OBTENER EL CODIGO
def get_code():
    url='https://github.com/login/oauth/authorize'
    params={
        'client_id':'dff5a77e6538da07aecf',
        'scope':'user'
    }
    
    response=requests.get(url,params=params)
    return response.url
    
##OBTENER EL TOKEN
def get_token(code):
    url='https://github.com/login/oauth/access_token'
    
    params = {
        'client_id':'dff5a77e6538da07aecf',
        'client_secret':'71a0b9c31bf90ef840beca35866c6e962ad9e5fb',
        'code':code
    }
    
    headers={
        'Accept': 'application/json'
    }
    
    response=requests.post(url,params=params,headers=headers)
    if response.status_code==200:
        payload=response.json()
        return payload.get('access_token')

##OBTENER EL USUARIO

def get_usser(access_token):
    url='https://api.github.com/user'
    headers={
        'Accept': 'application/vnd.github+json',
        'Authorization': f"Bearer {access_token}"
    }
    
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.json()



if __name__=='__main__':
    url=get_code()
    webbrowser.open(url)
    
    code=input('ingresa el codigo: ')
    code=code.strip().replace('\n','')
    
    access_token=get_token(code)
    
    user=get_usser(access_token)
    print(user.get('login'))