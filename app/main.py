from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.strip() or not host.replace('.', '').isnumeric():
        return {"error": "Host parameter is empty, invalid, or contains non-numeric characters"}
    args = ['ping', f'{host}']
    try:
        subprocess.run(args, check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}