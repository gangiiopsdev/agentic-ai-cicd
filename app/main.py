from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement logic to validate the host string
    return all(c.isalnum() or c in ('.', '-') for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"error": "Invalid host"}, 400
    
    # Secure implementation
    subprocess.run(["ping", host], check=True)
    
    return {"status": "completed"}