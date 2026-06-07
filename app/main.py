from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        host = shlex.quote(host)  # Sanitize input to prevent injection
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}