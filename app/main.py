from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    allowed_hosts = ['example.com', 'test.example.com']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        raise ValueError("Host not allowed")

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    import shlex
    host_shlexed = shlex.quote(host)
    try:
        result = subprocess.run(['ping', host_shlexed], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}