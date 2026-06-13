from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate and sanitize host input
        if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
            raise ValueError('Invalid host name')
        output = subprocess.run(['/usr/bin/ping', host], check=True, stdout=subprocess.PIPE)
        return output.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}