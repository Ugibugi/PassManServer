import logging
from flask import Flask,request,json
import models, utils
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
models.db.init_app(app)
models.db.create_all()

@app.route("/vault/new", methods = ['POST'])
def create_vault():
    j = json.loads(request.data)
    data = j['data']
    utils.insert_new_vault(data['public_key'],data['name'])
    return json.jsonify(utils.success())

@app.route("/vault/get", methods = ['POST'])
def get_vault():
    j = json.loads(request.data)
    data = j['data']
    plist = utils.get_passwords(data['public_key'])
    return json.jsonify(utils.success({'keys':plist}))

@app.route("/pass/add", methods = ['POST'])
def add_pass():
    j = json.loads(request.data)
    data = j['data']
    plist = utils.insert_new_password(data['public_key'],data['name'],data['value'])
    return json.jsonify(utils.success())

@app.errorhandler(404)
def error404(e):
    return json.jsonify({'status':e}), 404

@app.errorhandler(400)
def error404(e):
    return json.jsonify({'status':e}), 400