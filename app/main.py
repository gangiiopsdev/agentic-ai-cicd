from fastapi import FastAPI
import subprocess
def validate_host(host):
    # Add your validation logic here (e.g., allowed hosts list)
    if host not in ['example.com', 'localhost']:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = ['ping', '-c', '1', host]  # Use the -c option to limit the number of pings
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}