from fastapi import FastAPI
import subprocess
def ping(host: str):
    args = ['ping', '-c', '1', host]  # Limiting the number of pings to reduce risk
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/ping/{host}')
def read_ping(host: str):
    return ping(host)