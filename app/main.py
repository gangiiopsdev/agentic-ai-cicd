from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '._-')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    # Use a safe subprocess call
    result = subprocess.run(['ping', '--{}'.format(escaped_host)], check=True, capture_output=True)
    return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}