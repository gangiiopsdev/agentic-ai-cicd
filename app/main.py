from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if validate_host(host):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.output.decode()}
    else:
        return {'status': 'error', 'output': 'Invalid host'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Implement validation logic here
    return True