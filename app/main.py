from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_host(host):
    try:
        response = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE)
        return {"status": "completed", "response": response.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping(host: str):
    return ping_host(host)