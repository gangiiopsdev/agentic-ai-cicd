from fastapi import FastAPI
import subprocess
import shlex

allowed_hosts = {'example.com', 'test.com'}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if host in allowed_hosts:
        try:
            result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True, timeout=5)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Host not allowed"}