from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        return {"status": "invalid host"}
    # Use check_output instead of call for better control and error handling
    try:
        output = subprocess.check_output(["ping", host], shell=False, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)