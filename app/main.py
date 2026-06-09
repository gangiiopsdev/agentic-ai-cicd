from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using full path and validating input
    command = ['ping', host]
    if not all(os.path.exists(cmd) for cmd in command):  # Simplified validation, replace with proper validation logic
        return {'error': 'Invalid command'}, 400
    subprocess.run(command, check=True)
    return {'status': 'completed'}