from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Using check_output instead of call and avoiding shell=True for safety
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Failed to ping {host}: {e.output.decode('utf-8')}"

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}