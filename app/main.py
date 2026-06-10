from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input and use full path for 'ping'
    safe_host = host.strip().replace(';', '').replace('&', '')
    try:
        output = subprocess.check_output(['/bin/ping', '-c', '1', safe_host], stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}