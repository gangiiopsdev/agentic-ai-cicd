from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Input validation
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}