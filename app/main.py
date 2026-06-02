from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isdigit() or len(host) > 15:
        return {'error': 'Invalid host'}, 400
    try:
        result = subprocess.run(['ping', '-c', str(1), host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': 'Ping failed', 'details': e.stderr}, 500
    except Exception as e:
        return {'error': 'An unexpected error occurred', 'details': str(e)}, 500