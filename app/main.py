from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Implement validation logic here
    pass

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host], shell=False)
        return {"status": "completed"}
    else:
        return {"status": "invalid host"}