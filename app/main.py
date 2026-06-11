from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.allowed_hosts = {'example.com', 'another-example.com'}
    def safe_ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError('Host not allowed')
        args = shlex.split(f"ping {host}")
        subprocess.run(args, check=True)
app = FastAPI()
safe_ping_instance = SafePing()
async def is_safe_host(host: str) -> bool:
    return safe_ping_instance.host_allowed(host)
@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=403, detail="Invalid host")
safe_ping_instance.safe_ping(host)
return {"status": "completed"}