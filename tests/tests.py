import requests

mainURL = 'http://localhost:3000'

def req(endpoint,payload):
    finalURL = mainURL+endpoint
    print(f'Sending request to {finalURL} with: \n {payload}')
    res = requests.post(mainURL+endpoint,json=payload)
    print(f'Got response: {res.content}')


#test create vault

req('/vault/new', {
    'data':{
        'public_key':"gggggggggggggggggggggggggg",
        'name':'aaaaaaaaaaaaaaaaaaaaaaaaaa'
    },
    'hmac':'fgfgfgfgfgfgfgfgfgfgfgfg'
})


