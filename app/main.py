from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', host], shell=False, stderr=subprocess.STDOUT)
        return {'host': host, 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'host': host, 'error': e.output.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)