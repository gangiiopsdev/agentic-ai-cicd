from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Sanitize the host input by removing potentially harmful characters
    safe_host = ''.join(c for c in host if c.isalnum() or c in '._-')
    try:
        args = ['ping', '-c', '1'] + shlex.split(safe_host)
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)