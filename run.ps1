$env:FLASK_APP = "src/main"
python -m flask run --host=0.0.0.0 -p 3000 #--cert=certs/cert.pem --key=certs/key.pem