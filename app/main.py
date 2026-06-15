from fastapi import FastAPI
import subprocess

app = FastAPI()

def create_safe_ping_command(host):
    # Use a list for the command, avoiding shell=True
    return ['ping', host]

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(create_safe_ping_command(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}