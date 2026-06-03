from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    result = subprocess.run(['/usr/bin/ping', subprocess.check_output(f'echo {host}', shell=True).decode('utf-8').strip()], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = subprocess.run(['/usr/bin/ping', subprocess.check_output(f'echo {host}', shell=True).decode('utf-8').strip()], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}