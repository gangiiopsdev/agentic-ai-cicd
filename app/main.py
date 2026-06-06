from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use a whitelist of allowed hosts instead of sanitization
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Use a full path for the executable to mitigate risks
        result = subprocess.run(['/usr/bin/ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}