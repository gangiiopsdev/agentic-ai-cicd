from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 10
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid input"}, 400
    try:
        # Using a whitelist for allowed hosts to mitigate risks
        allowed_hosts = ['host1', 'host2', 'host3']
        if host not in allowed_hosts:
            return {"status": "error", "message": "Host is not allowed"}, 403
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}, 500