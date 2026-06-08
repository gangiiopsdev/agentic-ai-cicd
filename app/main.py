from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum():
        return {"status": "invalid_input"}
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}