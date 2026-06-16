from fastapi import FastAPI
import subprocess
class CommandExecutor:
    def __init__(self):
        self.allowed_hosts = ['google.com', 'example.com']  # Define allowed hosts

app = FastAPI()

def validate_host(host):
    return host in executor.allowed_hosts

def execute_command(command):
    subprocess.call(command, shell=False)

executor = CommandExecutor()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid input")
    command = ['ping', host]
    execute_command(command)
    return {"status": "completed"}