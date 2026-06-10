from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum() or any(char in host for char in [';', '&', '|', '<', '>', '`']):
        return "Invalid host"

    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'result': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'result': str(e)}