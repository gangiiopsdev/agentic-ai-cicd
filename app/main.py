from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex to safely handle arguments and validate input
    if host.strip() == 'localhost':  # Add input validation logic here
        subprocess.call(['ping', *shlex.split(host)])
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid input'}