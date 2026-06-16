from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with absolute path to avoid shell execution
    try:
        result = subprocess.run(['/bin/ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}