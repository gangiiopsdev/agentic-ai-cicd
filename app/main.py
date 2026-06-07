from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_host(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = ping_host(host)
    return {"status": "completed", "result": result}