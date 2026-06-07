from fastapi import FastAPI
import subprocess
cimport os
def safe_ping(host):
    if not host:
        return False
    cmd = ["ping", host]
    try:
        output = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)
class SafePingFastAPI(FastAPI):
    @app.get="/ping")
    def ping(host: str = None):
        result = safe_ping(host)
        if result:
            return {"status": "completed", "result": result}
        else:
            return {"status": "failed", "reason": "Invalid host or ping command failed"}