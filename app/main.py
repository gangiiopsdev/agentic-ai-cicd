from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    return host.isalnum() and len(host) <= 255

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"error": "Invalid input"}, 400
    # Sanitize the host input to prevent injection attacks
    sanitized_host = subprocess.quote(host)
    args = ['ping', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}