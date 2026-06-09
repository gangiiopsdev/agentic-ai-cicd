from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
            raise ValueError('Invalid hostname')
        output = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return ping(host)