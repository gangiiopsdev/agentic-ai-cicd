from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'localhost']

    def safe_ping(self, host: str):
        if host not in self.allowed_hosts:
            return 'Host not allowed'
        try:
            args = shlex.split(f'ping -c 1 {host}')
            output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
            return output.decode('utf-8')
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            return str(e)

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    result = safe_ping_instance.safe_ping(host)
    return {'status': 'completed', 'result': result}