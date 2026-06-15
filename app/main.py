from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.hosts = set()

    def add_host(self, host: str):
        if not self.is_safe(host):
            raise ValueError('Unsafe host provided')
        self.hosts.add(host)

    def is_safe(self, host: str) -> bool:
        # Implement a whitelist of allowed hosts or patterns
        return 'example.com' in host

    async def safe_ping(self, host: str):
        if not self.is_safe(host):
            raise ValueError('Unsafe host provided')
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()
ping_service = SafePing()

@app.get("/ping")
def ping(host: str):
    if host not in ping_service.hosts:
        ping_service.add_host(host)
    output = ping_service.safe_ping(host)
    return output