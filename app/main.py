from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input
    if not host.isdigit() or len(host) > 15:
        return "Invalid host"
    try:
        result = subprocess.run(["ping", host], shell=False, check=True, capture_output=True, text=True)
        return {"status": "Success", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "Failure", "error": str(e)}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return result