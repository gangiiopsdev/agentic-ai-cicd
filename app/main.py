from fastapi import FastAPI
import subprocess
import re
def validate_ip(ip):
    return ip.replace('.', '').isnumeric() and len(ip.split('.')) == 4

@app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_ip(host):
        return {"status": "failed", "error": "Invalid IP address"}
    cmd = ['ping', re.escape(host)]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "message": "Request timed out"}