from fastapi import FastAPI
import subprocess
cimport = __import__

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', '--count=1', host]  # Add a count parameter to limit the number of pings
    subprocess.run(command, check=True, shell=False)
    return {'status': 'completed'}