from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    if not all(c in allowed_chars for c in host):
        raise ValueError("Invalid host name")
    command = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {
            "status": "completed",
            "output": result.stdout
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": e.stderr
        }
global_config = {
    'host': '127.0.0.1',
    'port': 8000,
}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if host == global_config['host']:
        try:
            response = safe_ping(host)
            return response
        except subprocess.CalledProcessError as e:
            return {
                "status": "failed",
                "error": str(e)
            }
    else:
        return {
            "status": "failed",
            "error": "Invalid host"
        }