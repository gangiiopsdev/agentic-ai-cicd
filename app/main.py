from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use a list for the command and avoid shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class PingEndpoint:
    @staticmethod
def ping(host: str):
        # Call the safe_ping function
        status = safe_ping(host)
        return {'status': 'completed', 'result': status}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    # Validate and sanitize the host parameter
    if not host.strip():
        raise ValueError('Host parameter cannot be empty')
    return PingEndpoint.ping(host)