from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using shlex.quote to escape shell metacharacters and validate input
    if not host or ' ' in host or ';' in host:
        raise ValueError('Invalid host name')
    safe_host = subprocess.shlex_quote(host)
    try:
        subprocess.run(['ping', safe_host], check=True, timeout=5)  # Add a timeout for security
    except subprocess.TimeoutExpired:
        return {'status': 'timeout'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping/{host}')
def ping(host: str):
    return ping(host)