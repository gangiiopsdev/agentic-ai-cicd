from fastapi import FastAPI
import subprocess

def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = execute_ping(host)
        return result
    except Exception as e:
        return {'status': 'error', 'error': str(e)}