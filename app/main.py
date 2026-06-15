from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate host input to ensure it is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    result = safe_ping(host)
    return {"status": "completed", "result": result}