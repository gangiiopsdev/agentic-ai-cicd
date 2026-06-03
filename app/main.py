from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> bool:
    if not host.isdigit():
        return False
    # Additional checks for valid IP address or hostname can be added here
    return True

@app.get("/ping")
def ping(host: str):
    if not sanitize_host(host):
        return {"error": "Invalid host input"}
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}