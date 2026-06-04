from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Basic input validation to prevent command injection
        raise ValueError("Invalid input for hostname")
    return {'status': 'completed', 'output': safe_ping(host)}