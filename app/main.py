from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Input validation and escaping
    if not host.isalnum() or len(host) > 10:
        return {'error': 'Invalid input'}, 400
    args = ['ping', '-c', '1', host]  # Use '-c' to limit the number of pings
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}