from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True, timeout=5)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}

@app.get="/ping")
def ping_route(host: str):
    return ping(host)