from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, shell=False)
    except subprocess.CalledProcessError as e:
        output = e.output
    return jsonable_encoder({'status': 'completed', 'output': output.decode('utf-8')})