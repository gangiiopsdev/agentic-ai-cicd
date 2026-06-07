from fastapi import FastAPI
import subprocess
def _ping(host):
    args = ['ping', '--count=1', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class SafeHostValidator:
    @staticmethod
def validate_host(host):
        valid_hosts = ['localhost', '127.0.0.1', '::1']
        if host in valid_hosts:
            return True
        return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if SafeHostValidator.validate_host(host):
        try:
            result = _ping(host)
            return {"status": "completed", "output": result}
        except Exception as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Invalid host"}