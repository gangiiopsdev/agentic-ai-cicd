from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Safer implementation using subprocess.run with args instead of shell=True
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    execute_ping(host)