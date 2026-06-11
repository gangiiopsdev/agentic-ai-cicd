from fastapi import FastAPI
import subprocess
def sanitize_host(host: str) -> str:
    # Add your sanitization logic here (e.g., allow only specific domains)
    return host.strip()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        result = subprocess.run(["/bin/ping", sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}