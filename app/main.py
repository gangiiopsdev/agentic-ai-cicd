from fastapi import FastAPI
import subprocess
globals = {'host': str}
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        if host in globals.values():
            result = subprocess.call(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
        else:
            return {'status': 'error', 'message': 'Invalid host'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}