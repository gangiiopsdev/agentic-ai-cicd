from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Validate the host input to ensure it only contains allowed characters
    if not all(char.isalnum() or char in ['.', '-', '_'] for char in host):
        return {'status': 'failed', 'error': 'Invalid host name'}

    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)