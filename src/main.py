import logging
from os import abort
from flask import Flask,request,json
import models, utils
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
models.db.init_app(app)
models.db.create_all()

@app.route("/",methods = ['GET'])
def hello_screen():
    return "Server is running"

@app.route("/vault/new", methods = ['POST'])
def create_vault():
    logging.error("Got REQ: " + str(request.json))
    data = request.json['data']
    if utils.verify_signature(data,data['public_key'],request.json['sign']):
        utils.insert_new_vault(data['public_key'],data['name'])
        return json.jsonify(utils.success())
    else:
       return error400("Wrong signature")


@app.route("/vault/get", methods = ['POST'])
def get_vault():
    logging.error("Got REQ: " + str(request.json))
    data = request.json['data']
    if utils.verify_signature(data,data['public_key'],request.json['sign']):
        plist,name = utils.get_passwords(data['public_key'])
        return json.jsonify(utils.success({'keys':plist, 'name':name}))
    else:
        return error400("Wrong signature")

@app.route("/pass/add", methods = ['POST'])
def add_pass():
    logging.error("Got REQ: " + str(request.json))
    data = request.json['data']
    if utils.verify_signature(data,data['public_key'],request.json['sign']):
        utils.insert_new_password(data['public_key'],data['name'],data['value'])
        return json.jsonify(utils.success())
    else:
        return error400('Wrong signature')

@app.errorhandler(404)
def error404(e):
    return json.jsonify({'status':str(e)}), 404

@app.errorhandler(400)
def error400(e):
    return json.jsonify({'status':str(e)}), 400