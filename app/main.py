from fastapi import FastAPI
import subprocess
import re
def run_ping(host: str):
    # Regular expression to validate host as a numeric IP address or hostname
    ip_pattern = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'
    hostname_pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])*$'

    if not (re.match(ip_pattern, host) or re.match(hostname_pattern, host)):
        raise ValueError('Invalid input')

    output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': output.stdout}

except subprocess.CalledProcessError as e:
    return {'status': 'failed', 'error': str(e)}
except ValueError as ve:
    return {'status': 'failed', 'error': str(ve)}

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return run_ping(host)