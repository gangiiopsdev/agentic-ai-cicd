from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    try:
        subprocess.call(['ping', host], shell=False)
    except Exception as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    result = ping_safe(host)
    if 'error' in result:
        return result
    else:
        return {'status': 'completed'}