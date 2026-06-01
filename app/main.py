from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and use of shlex.quote
    if all(c.isalnum() or c in ('-', '.', '_') for c in host):  # Basic validation of the hostname
        subprocess.run(['ping', shlex.quote(host)], check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid hostname'}, 400