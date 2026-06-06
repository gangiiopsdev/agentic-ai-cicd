from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use subprocess.Popen instead of subprocess.call and avoid shell=True for better security.
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode()

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in '.-' for c in host):
        return {"status": "error", "message": "Invalid host name"}
    output, error = safe_ping(host)
    if error:
        return {"status": "error", "message": error}
    return {"status": "completed", "output": output}