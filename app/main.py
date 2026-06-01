from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Secure implementation
    subprocess.call(["ping", host], shell=False)

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    # Secure implementation
    try:
        subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}