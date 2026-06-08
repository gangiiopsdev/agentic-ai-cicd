from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> dict:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if all(c in allowed_chars for c in host):
        try:
            args = ['ping', '-c', '1'] + [shlex.quote(arg) for arg in shlex.split(host)]
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}
    else:
        return {'status': 'invalid_host'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)