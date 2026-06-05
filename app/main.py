from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'test.com']

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    # Secure implementation using subprocess.run with shell=False
    args = ["ping", host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.stderr.decode()}