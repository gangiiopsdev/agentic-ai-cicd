from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.replace('.', '', 3).isdigit():
        return True
    else:
        return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"error": "Invalid host"}

    # Safe implementation using subprocess.run with shell=False and executable parameter
    result = subprocess.run(['ping', '-c', '1', host], check=True, text=True)

    return {"status": "completed", "result": result.stdout}