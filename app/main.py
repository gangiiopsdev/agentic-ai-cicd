from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Implement proper validation logic here
    return all(c.isalnum() or c in '.-_' for c in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "invalid host"}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}