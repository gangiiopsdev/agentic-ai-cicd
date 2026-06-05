from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to ensure it does not contain malicious content
        if not host.isalnum():
            raise ValueError("Invalid host")
        output = subprocess.check_output(['ping', host], shell=False, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}