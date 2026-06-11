from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return all(c.isalnum() or c in ('.', '-') for c in host)

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}, 400
    else:
        return {'error': 'Invalid host'}, 400