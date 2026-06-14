from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate the host input to ensure it does not contain malicious characters
        if '@' in host or '%' in host or '&&' in host or ';' in host or '$(' in host or ')' in host or '|' in host or '&' in host:
            return {'status': 'error', 'message': 'Invalid input'}
        subprocess.run(['ping', '-c 1', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    return ping(host)