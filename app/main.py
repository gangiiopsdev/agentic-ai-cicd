from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it only contains valid characters
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    output = execute_ping(host)
    return {'status': 'completed', 'output': output}