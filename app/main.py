from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', '-c', '1', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = host.replace(';', '').replace('&', '')
    response = safe_ping(sanitized_host)
    return {'status': 'completed', 'output': response}