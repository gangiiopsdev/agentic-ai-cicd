from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> None:
    try:
        subprocess.call(['ping', host], shell=False)
    except Exception as e:
        print(f'Error pinging {host}: {e}')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}