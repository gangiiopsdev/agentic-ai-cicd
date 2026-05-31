from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_command(command: str) -> list:
    return shlex.split(command)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    try:
        result = subprocess.run(safe_command(f'ping -c 1 {host}'), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}