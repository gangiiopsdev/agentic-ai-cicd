from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host and all(c.isalnum() or c in ('.', '-', '_') for c in host):
        args = ['ping', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Invalid hostname')