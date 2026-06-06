from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Validate the host to prevent injection attacks
        if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
            raise ValueError('Invalid host name')
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    sanitized_host = ''.join(c for c in host if c.isalnum() or c in ['.', '-', '_'])
    return safe_ping(sanitized_host)