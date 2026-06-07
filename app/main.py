from fastapi import FastAPI
import subprocess

globals = {'host': str}
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        if host in globals.values():
            result = subprocess.run(['ping', host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'error', 'message': 'Invalid host'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}