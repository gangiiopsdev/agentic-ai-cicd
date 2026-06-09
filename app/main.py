from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr, 'utf-8')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)