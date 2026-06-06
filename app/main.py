from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host name'}
    
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.output}
    return {'status': 'completed', 'output': output}