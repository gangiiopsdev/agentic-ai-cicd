from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            # Use shlex.quote to safely escape the host parameter
            safe_host = shlex.quote(host)
            subprocess.call(f"ping {safe_host}", shell=False)
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}
app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return SafePing.ping(host)