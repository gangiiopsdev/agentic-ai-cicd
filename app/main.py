from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Safe implementation using subprocess.run with full path for the executable and input validation
        if host and all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
            result = subprocess.run(['/bin/ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            raise ValueError('Invalid host input')
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'error', 'error': str(e)}