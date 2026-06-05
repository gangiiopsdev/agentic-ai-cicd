from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host format
    if not host.isdigit():
        return {"error": "Invalid host format"}

    # Use absolute path for 'ping' command to mitigate risks
    subprocess.run(['/bin/ping', host], check=True)

    return {"status": "completed"}