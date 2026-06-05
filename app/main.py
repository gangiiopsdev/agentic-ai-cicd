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
    output, error = safe_ping(host)
    if error:
        return {"status": "error", "message": error}
    return {"status": "completed", "output": output}