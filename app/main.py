from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    try:
        subprocess.run(['ping', host], check=True)
        return True
    except subprocess.CalledProcessError as e:
        return False

@app.get("/ping")
def ping(host: str):