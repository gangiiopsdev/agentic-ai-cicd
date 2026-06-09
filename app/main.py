from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        # Sanitize host input
        host = subprocess.check_output(['echo', host], text=True).strip()
        subprocess.run(['ping', '-c', '1', host], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e}')
        return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if execute_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}