from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}