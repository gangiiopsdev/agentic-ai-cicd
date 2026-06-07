from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        # Safe implementation using subprocess.run with shell=False and check=True
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}