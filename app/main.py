from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Safe implementation using subprocess.run with shell=False
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def execute_command(command):
    # Generic function for safe command execution
    try:
        result = subprocess.run(command, shell=False, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)