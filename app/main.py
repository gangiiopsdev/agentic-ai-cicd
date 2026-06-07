from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with argument sanitization and exception handling
    try:
        # Sanitize the input to prevent command injection
        sanitized_host = host.replace(';', '').replace('&', '')
        subprocess.call(['ping', '-c', '1', sanitized_host], shell=False)  # Limiting the number of pings to one
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}