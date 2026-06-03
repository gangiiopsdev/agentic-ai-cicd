from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.ping_command = 'ping'

    def safe_ping(self, host, count=4):
        try:
            args = [self.ping_command] + ['-c', str(count), host]
            output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e.output)

app = FastAPI()
ping_service = SafePing()

@app.get("/ping")
def ping(host: str):
    result = ping_service.safe_ping(host)
    return {'status': 'completed', 'result': result}