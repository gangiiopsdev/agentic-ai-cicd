from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str):
    # Implement a whitelist of allowed hosts or perform additional validation
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')
@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        command = ["ping", shlex.quote(host)]  # Use shlex.quote to escape the host parameter
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}