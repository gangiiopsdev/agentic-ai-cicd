from fastapi import FastAPI
import subprocess
import shlex
import re
def ping(host: str):
    try:
        # Use regular expression to validate the host input
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid input')
        args = ['ping', '-c', '1', host]  # Limit ping count for security
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    # Validate input to ensure it does not contain unexpected characters or commands
    if not host.isalnum() and '-' not in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)