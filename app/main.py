from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def validate_input(input_value):
    allowed_hosts = ['localhost', '127.0.0.1']
    if input_value not in allowed_hosts:
        raise ValueError("Invalid host")

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):\n    validate_input(host)
    cmd = ["ping", host]\n    result = run_command(cmd)\n    return {"status": "completed", "output": result}