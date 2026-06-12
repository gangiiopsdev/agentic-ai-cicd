from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.hosts = []

    def update_hosts(self, new_hosts):
        self.hosts.extend(new_hosts)

    def ping_host(self, host):
        try:
            args = ['ping', '-c', '1', shlex.quote(host)]
            subprocess.run(args, check=True, timeout=1)
            return True
        except subprocess.CalledProcessError as e:
            print(e)
            return False
        except Exception as e:
            print(e)
            return False

app = FastAPI()
pinger = SafePing()

def update_hosts(hosts):
    pinger.update_hosts(hosts)

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "failed", "message": "Invalid input"}
    if pinger.ping_host(host):
        return {"status": "completed", "message": "Ping successful"}
    else:
        return {"status": "failed", "message": "Ping failed"}