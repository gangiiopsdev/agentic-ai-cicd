from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def get_ping_status(host: str):  # Add host parameter to the function signature
    if host.strip() and all(c.isalnum() for c in host):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout,
    else:
        return None