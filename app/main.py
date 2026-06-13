from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize user input to prevent command injection
    if not host.replace('.', '').isdigit():
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        output = subprocess.check_output(['ping', host], timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}