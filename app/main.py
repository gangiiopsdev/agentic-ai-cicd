from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        if '1 received' in result.stdout:
            return True
        else:
            print(f'Ping failed: {result.stderr}')
            return False
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}
{e.stderr}')
        return False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}