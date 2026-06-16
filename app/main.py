from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):