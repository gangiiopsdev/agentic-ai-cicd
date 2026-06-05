from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation to avoid shell injection and ensure safe execution
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}