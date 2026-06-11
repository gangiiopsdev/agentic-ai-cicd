from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    if not host.isnumeric():
        return "Invalid input"
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)