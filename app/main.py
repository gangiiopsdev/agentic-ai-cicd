from fastapi import FastAPI
import subprocess
import re
def sanitize_input(input_string):
    # Implement a more robust sanitization logic here
    return ''.join(e for e in input_string if e.isalnum() or e in ['-', '.', '_', '@', '#'])

def validate_host(host):
    # Regular expression to allow only valid hostnames
    pattern = re.compile(r'^[a-zA-Z0-9-.]+$')
    return bool(pattern.match(host))

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid input"}
    sanitized_host = subprocess.quote(sanitize_input(host))
    result = subprocess.run(['ping', '-c', '1', f'"{sanitized_host}"'], capture_output=True, text=True)
    return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}