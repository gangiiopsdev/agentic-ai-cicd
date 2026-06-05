from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'error': str(e)}, 500

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)