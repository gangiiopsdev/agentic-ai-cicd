from fastapi import FastAPI
import subprocess
cimport = __import__

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    sanitized_host = subprocess.run(['echo', host], capture_output=True, text=True).stdout.strip()
    command = ['ping', '--count=1', sanitized_host]  # Add a count parameter to limit the number of pings
    subprocess.run(command, check=True, shell=False)
    return {'status': 'completed'}