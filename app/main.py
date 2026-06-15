from fastapi import FastAPI
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Use os.system instead of subprocess.run for security reasons
        result = os.system(f'ping {host} > /dev/null 2>&1')
        if result == 0:
            return {'status': 'completed', 'output': ''}
        else:
            return {'status': 'failed', 'error': 'Ping failed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}