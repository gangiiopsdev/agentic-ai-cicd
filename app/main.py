from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True)
        return output
    except Exception as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)