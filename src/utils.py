import json, hmac, hashlib
import models

ERROR_MESSAGES = ['success','Missing arguments', 'Vault not found', 'Authentication failure (hmac)']

def compute_hmac(object,pubk):
    s = json.dumps(object, separators = (',',':'))
    h = hmac.new(pubk.encode(),s.encode(),hashlib.sha256)
    return h.hexdigest()

def insert_new_vault(pubk,name):
    v = models.Vault(pubk,name)
    models.db.session.add(v)
    models.db.session.commit()

def get_passwords(public_key):
    v = models.Vault.query.filter_by(pubk=public_key).first_or_404(description='Vault not found')
    result = []
    for p in v.passwords:
        result.append({'name':p.name,'value':p.value})
    return result

def insert_new_password(public_key,name,value):
    v = models.Vault.query.filter_by(pubk=public_key).first_or_404(description='Vault not found')
    p = models.Password(name,value,v.id)
    models.db.session.add(p)
    models.db.session.commit()

def success(object = None):
    return {'data':object,'status':'success'}





