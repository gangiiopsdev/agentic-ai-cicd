from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Define allowed hosts or implement more complex validation
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return True, output.decode()
    except subprocess.CalledProcessError as e:
        return False, e.output.decode()

@app.get("/ping")
def ping(host: str):
    success, result = safe_ping(host)
    if success:
        return {"status": "completed", "output": result}
    else:
        return {"status": "failed", "error": result}