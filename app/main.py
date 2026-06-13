from fastapi import FastAPI
import subprocess

def execute_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call for better security
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = host.replace(';', '').replace('&', '').replace('|', '')
    return execute_ping(sanitized_host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}