from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command):
    return subprocess.call(command)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command = ["ping", host]
    return execute_command(command)