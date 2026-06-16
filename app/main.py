from fastapi import FastAPI
import subprocess
from shlex import quote

def execute_safe_command(command):
    args = [quote(arg) for arg in command.split() if arg.strip()]  # Ensure no empty strings and sanitize input
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_command = f'ping -c 1 {quote(host)}'
    output = execute_safe_command(safe_command)
    return {'status': 'completed', 'output': output}