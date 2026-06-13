from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input
    if not host.replace('.', '').isdigit():
        return {"status": "failed", "error": "Invalid hostname"}
    try:
        result = subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}

# Preventive controls:
# 1. Use parameterized commands to avoid shell injection.
# 2. Validate and sanitize user input more strictly.
# 3. Consider using a whitelist of allowed hosts.