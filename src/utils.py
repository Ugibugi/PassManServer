import json, hmac, hashlib
import models
from base64 import b64decode

ERROR_MESSAGES = ['success','Missing arguments', 'Vault not found', 'Authentication failure (hmac)']

def to_int(b64str):
    return int(b64decode(b64str).hex(),16)


def verify_signature(object,pubk,sign):
    '''Dokonuje weryfikacji poprawności przesłanego podpisu wiadomości'''
    mess = json.dumps(object, separators = (',',':'))
    from Crypto.PublicKey import RSA
    from Crypto.Signature import PKCS1_v1_5 as PKCS
    from Crypto.Hash import SHA512
 

    kmod = pubk.split('#')


    key = RSA.construct((to_int(kmod[0]),to_int(kmod[1])))
    signer = PKCS.new(key)
    digest = SHA512.new()
    digest.update(mess.encode('utf-8'))

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

    if object is None:
        return {'status':'success'}
    else:
        return {'data':object,'status':'success'}





