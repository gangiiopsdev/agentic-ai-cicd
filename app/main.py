from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    return run_ping(host)