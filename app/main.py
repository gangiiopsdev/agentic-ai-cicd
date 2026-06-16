from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command, args):
    result = subprocess.run([command] + args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip() and all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        result = run_command('ping', [host])
    else:
        return {'status': 'error', 'message': 'Invalid host'}
    return result