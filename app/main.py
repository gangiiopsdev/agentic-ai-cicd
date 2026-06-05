from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, host))

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    if escaped_host != host:
        return {"status": "error", "message": "Invalid characters in host name"}
    try:
        result = subprocess.run(['ping', '-c', '1'] + shlex.split(escaped_host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}