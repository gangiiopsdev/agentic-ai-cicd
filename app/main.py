from fastapi import FastAPI
import subprocess
def safe_ping(host):
    cmd = ['ping', host]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it is a valid hostname or IP address
    if not validate_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    return safe_ping(host)

def validate_host(host):
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))