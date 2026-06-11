from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Ensure host input is validated and sanitized
    if '@' in host or ' ' in host:
        return {'error': 'Invalid input'}, 400
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}