from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Sanitize the host input
        if not all(c.isalnum() or c in ('.', '-') for c in host):
            raise ValueError('Invalid host')
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def is_valid_host(host: str) -> bool:
    # Simple validation logic, replace with more robust checks as needed
    return all(c.isalnum() or c in ('.', '-') for c in host)