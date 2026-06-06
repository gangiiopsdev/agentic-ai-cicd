from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate the host to ensure it is a valid IP or hostname
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host')
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)