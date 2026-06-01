from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    return host.isalnum()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid input"}
    args = ['ping', host]
    try:
        subprocess.run(args, check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}