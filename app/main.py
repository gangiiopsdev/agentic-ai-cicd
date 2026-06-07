from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, allowed_hosts):
        self.allowed_hosts = allowed_hosts

    def run(self, host):
        if host in self.allowed_hosts:
            try:
                result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
                return {"status": "completed", "output": result.stdout}
            except subprocess.CalledProcessError as e:
                return {"status": "failed", "error": str(e)}
        else:
            return {"status": "failed", "error": "Host not allowed to ping"}

app = FastAPI()
allowed_hosts = ['example.com', '192.168.1.1']
ping_command = PingCommand(allowed_hosts)

@app.get("/ping")
def ping(host: str):
    return ping_command.run(host)