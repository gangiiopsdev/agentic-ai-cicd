from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    try:
        response = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return response.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = _ping(host)
    return {"status": "completed", "result": result}