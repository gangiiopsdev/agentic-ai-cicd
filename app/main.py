from fastapi import FastAPI
import subprocess
import re
class SafePing:
    @staticmethod
def safe_ping(host):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
            return output.decode().strip()
        except subprocess.CalledProcessError as e:
            return str(e.output).decode().strip()

app = FastAPI()

def sanitize_host(host):
    # Regular expression to validate the host format
    pattern = r'^[a-zA-Z0-9.-]{1,}$'
    if re.match(pattern, host):
        return host
    else:
        raise ValueError('Invalid host format')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    result = SafePing.safe_ping(sanitized_host)
    return {"status": "completed", "result": result}