from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}