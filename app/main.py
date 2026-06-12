from fastapi import FastAPI
import subprocess
global_host = '127.0.0.1' # Replace with a fixed or trusted host

app = FastAPI()

@app.get("/ping")
def ping_endpoint():
    try:
        result = subprocess.run(['ping', global_host], check=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}