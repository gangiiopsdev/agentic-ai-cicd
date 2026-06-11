from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid command injection
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host): raise ValueError('Invalid hostname')
    result = safe_ping(host)
    return {"status": "completed", "result": result}

# Add additional security controls such as using parameterized commands or a whitelist of allowed hosts.