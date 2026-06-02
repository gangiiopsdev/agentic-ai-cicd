from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host):
    # Implement robust sanitization logic here
    return re.sub(r'[^a-zA-Z0-9.-]', '', host.strip())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        output = subprocess.run(['ping', f'-c 1 {sanitized_host}'], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Example of a more robust sanitization function
def sanitize_host(host):
    import os
    if not os.path.basename(host) == host.strip():
        raise ValueError("Invalid hostname")
    return re.sub(r'[^a-zA-Z0-9.-]', '', host.strip())