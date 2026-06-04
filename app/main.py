from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Error: {e.output.decode("utf-8")}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent injection attacks
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'result': 'Invalid hostname'}
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}