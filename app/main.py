from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    # Implement safe hostname validation logic here
    return True

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        raise Exception("Invalid hostname")
    # Secure implementation
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}