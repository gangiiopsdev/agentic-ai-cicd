from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host or not isinstance(host, str) or len(host.strip()) == 0:
            raise ValueError('Invalid host')
        # Allow only alphanumeric characters and certain special characters for the hostname
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid hostname format')
        # Using subprocess.run with shell=False and list of arguments for security
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'
    except ValueError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}