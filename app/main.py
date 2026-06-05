from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent shell injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    output = execute_ping(host)
    return {'status': 'completed', 'output': output}