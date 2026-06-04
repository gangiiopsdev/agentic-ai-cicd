from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {"status": "completed", "result": f'Ping to {host} was successful.'}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "result": e.output.decode('utf-8')}