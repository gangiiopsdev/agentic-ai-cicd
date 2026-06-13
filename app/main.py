from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        if result.returncode == 0:
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'error': result.stderr}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}