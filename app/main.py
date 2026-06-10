from fastapi import FastAPI
import subprocess
def escape_host(host):
    # Escape or validate host input here
    return ''.join(c for c in host if c.isalnum() or c in '-_.:~/')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        escaped_host = escape_host(host)
        subprocess.run(['ping', escaped_host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}