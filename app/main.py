from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Input validation
    if not host or len(host) > 255:
        return {
            "status": "error",
            "message": "Invalid host input"
        }

    result = safe_ping(host)

    return {"status": "completed", "result": result}