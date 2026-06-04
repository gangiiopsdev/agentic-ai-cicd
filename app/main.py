from fastapi import FastAPI
import subprocess
cimport os

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ('-', '.', '_', ':'))

def safe_ping(host):
    try:
        # Validate the host to ensure it only contains allowed characters and formats
        if not os.path.basename(host) == host or ':' not in host:
            raise ValueError('Invalid host format')
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    return safe_ping(safe_host)