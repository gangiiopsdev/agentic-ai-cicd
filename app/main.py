from fastapi import FastAPI
import subprocess
global allowed_hosts = ['example.com', 'another-example.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        # Use the full path of the executable to mitigate shell injection risks
        subprocess.run(["/bin/ping", host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400

def validate_host(host):
    # Implement a more secure and comprehensive host validation logic
    allowed_hosts = ['example.com', 'another-example.com']
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    if not re.match(pattern, host) or host not in allowed_hosts:
        return False
    return True