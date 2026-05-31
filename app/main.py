from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate input to prevent command injection
    valid_hosts = ['example.com', 'localhost']
    if host in valid_hosts:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    if output:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed"}