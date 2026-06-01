from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping'] + shlex.split(host)
    try:
        subprocess.run(args, check=True)
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
    return {'status': 'completed'}