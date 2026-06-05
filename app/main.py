from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command: str):
    try:
        output = subprocess.check_output(command, shell=True, timeout=5, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    command = f'ping -c 4 {host}'
    return run_command(command)