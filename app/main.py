from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Add your allowed hosts here
    if host in allowed_hosts:
        return True
    return False@app.get("/ping")def ping(host: str):
    if not validate_host(host):
        return {"error": "Invalid host"}, 400
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}, 500