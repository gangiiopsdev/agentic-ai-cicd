from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e.output)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isnumeric():  # Basic validation to avoid common pitfalls
        return {'status': 'error', 'message': 'Invalid input'}
    return safe_ping(host)