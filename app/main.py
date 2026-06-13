from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command: str):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Error: {e.output.decode('utf-8')}'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    result = execute_command(command)
    return {'status': 'completed', 'result': result}