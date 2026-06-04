from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run for better control and error handling
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters (e.g., alphanumeric, hyphen, dot)
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid input'}
    return safe_ping(host)