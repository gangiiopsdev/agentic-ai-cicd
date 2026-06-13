from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    cmd = ['ping'] + [h for h in shlex.split(host) if h.isalnum() or '_' in h]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout
class SafePingFilter:
    def __call__(self, host):
        if not all(c.isalnum() or c == '_' for c in host) or ' ' in host:
            raise ValueError("Invalid input")
        return safe_ping(host)
app = FastAPI()
@app.get("/ping")
def ping(host: str = SafePingFilter()):
    return host