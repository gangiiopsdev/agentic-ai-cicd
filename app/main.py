from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    allowed_hosts = ['example.com', 'another-example.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = ['ping', '--ipv4', host]  # Use --ipv4 to prevent DNS resolution, reducing risks
        subprocess.run(args, check=True)
    else:
        return {"status": "error", "message": "Invalid host"}
    return {"status": "completed"}