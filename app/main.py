from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping'] + shlex.split(host)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = shlex.quote(host)
    if not sanitized_host:
        return {'status': 'error', 'message': 'Invalid input'}
    success, message = safe_ping(sanitized_host)
    if not success:
        return {'status': 'error', 'message': message}
    return {'status': 'completed', 'output': message}