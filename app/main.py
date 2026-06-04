from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Validate host input to ensure it's not malicious
        if not validate_host(host):
            raise ValueError('Invalid host input')
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

def validate_host(host):
    # Implement validation logic here (e.g., regex pattern matching)
    import re
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        return True
    return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)