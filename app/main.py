from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.hosts = []

    def add_host(self, host: str):
        self.hosts.append(host)

    def safe_ping(self):
        results = {}
        for host in self.hosts:
            try:
                result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
                results[host] = result.stdout
            except subprocess.CalledProcessError as e:
                results[host] = f'Ping failed: {e}'
        return results

app = FastAPI()
ping_service = SafePing()

@app.get('/ping/{host}')
def ping(host: str):
    ping_service.add_host(host)
    return ping_service.safe_ping()