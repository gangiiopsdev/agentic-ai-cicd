from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_host(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': ping_host(host)}