from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError("Invalid hostname")
    args = ['ping', '--', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        raise Exception(f"Ping command failed: {error.decode('utf-8')})")
    return {"status": "completed", "output": output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}