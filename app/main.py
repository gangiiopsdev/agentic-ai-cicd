from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Using check_output instead of call for better error handling and to avoid shell=True
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)