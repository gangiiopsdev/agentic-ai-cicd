from fastapi import FastAPI
import subprocess
global_host = 'example.com'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.run(['ping', global_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}