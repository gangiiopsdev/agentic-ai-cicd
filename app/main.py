from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input
    if not (host.isalnum() or '.' in host):
        raise ValueError('Invalid hostname')

    # Sanitize the command arguments
    safe_command = ['ping', subprocess.check_output(['echo', host], text=True).strip()]
    try:
        subprocess.run(safe_command, check=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}