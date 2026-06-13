from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Sanitize input using subprocess.run with check_output and shell=False for safer execution
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return str(e.output)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or ' ' in host:
        raise ValueError('Invalid host name')
    return safe_ping(host)