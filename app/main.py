from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize the input to prevent command injection
        if not all(c.isalnum() or c in ' .-@' for c in host):
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}
    except ValueError as ve:
        return {'status': 'error', 'output': str(ve)}