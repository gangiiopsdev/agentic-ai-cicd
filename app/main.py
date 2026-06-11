from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return run_ping(host)