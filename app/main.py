from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']

    async def ping(self, host: str):
        if self._is_safe_host(host):
            try:
                result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
                return {"status": "completed", "output": result.stdout}
            except subprocess.CalledProcessError as e:
                return {"status": "failed", "error": e.stderr}
        else:
            return {"status": "failed", "error": "Host not allowed"}

    def _is_safe_host(self, host: str):
        return host in self.allowed_hosts
global_safe_ping = SafePing()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return global_safe_ping.ping(host)