from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        subprocess.call(['ping', host])
    except Exception as e:
        print(f'Error pinging {host}: {e}')

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}