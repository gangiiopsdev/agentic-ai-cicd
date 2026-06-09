from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    try:
        url = urlparse(host)
        if url.scheme or not all(c.isalnum() or c in '-.' for c in url.netloc):
            return {'status': 'error', 'output': 'Invalid input'}
        result = subprocess.run(['ping', url.netloc], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}
    except Exception as e:
        return {'status': 'error', 'output': str(e)}