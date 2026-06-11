from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        # Use subprocess.run for a safer alternative with proper shell quoting
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate host input to prevent command injection
    if not all(c in string.ascii_letters + string.digits for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return ping(host)