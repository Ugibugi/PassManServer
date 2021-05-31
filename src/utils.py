import json, hmac, hashlib
import models


ERROR_MESSAGES = ['success','Missing arguments', 'Vault not found', 'Authentication failure (hmac)']

def verify_signature(object,pubk,sign):
    '''Dokonuje weryfikacji poprawności przesłanego podpisu wiadomości'''
    mess = json.dumps(object, separators = (',',':'))
    from Crypto.PublicKey import RSA
    from Crypto.Signature import PKCS1_v1_5 as PKCS
    from Crypto.Hash import SHA256
    from base64 import b64decode

    key = RSA.importKey(b64decode(pubk))
    signer = PKCS.new(key)
    digest = SHA256.new()

    digest.update(mess)
    if signer.verify(digest, b64decode(sign)):
        return True
    else: 
        return False

def insert_new_vault(pubk,name):
    '''Tworzy nowy sejf'''
    v = models.Vault(pubk,name)
    models.db.session.add(v)
    models.db.session.commit()

def get_passwords(public_key):
    '''Zwraca listę haseł istniejących w danym sejfie'''
    v = models.Vault.query.filter_by(pubk=public_key).first_or_404(description='Vault not found')
    result = []
    for p in v.passwords:
        result.append({'name':p.name,'value':p.value})
    return result, v.name

def insert_new_password(public_key,name,value):
    '''Tworzy lub nadpisuje nowe hasło w danym sejfie '''
    v = models.Vault.query.filter_by(pubk=public_key).first_or_404(description='Vault not found')
    p = models.Password(name,value,v.id)
    models.db.session.add(p)
    models.db.session.commit()


def success(object = None):
    '''Zwraca dany obiekt wraz z polem informującym aplikacje o pozytywnym statusie zapytania'''
    return {'data':object,'status':'success'}





