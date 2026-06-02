from fastapi import FastAPI
import subprocess
def escape_shell_input(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '')

def safe_ping(host: str):
    try:
        # Use subprocess.run with list to avoid shell=True and command injection
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)