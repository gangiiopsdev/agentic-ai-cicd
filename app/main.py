from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:
        try:
            result = subprocess.run(['ping', '-c 4', host], capture_output=True, text=True, check=True)
            return {'status': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        raise ValueError('Ping to external hosts is not allowed')

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return result
    except ValueError as e:
        return {'error': str(e)}