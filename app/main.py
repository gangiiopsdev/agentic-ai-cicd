from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'localhost']

@app.get("/ping")
def ping(host: str):
    if host in allowed_hosts:
        cmd = ["ping", host]
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}
    else:
        return {"status": "failed", "error": "Host not allowed"}