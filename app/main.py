from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self, max_hops=4):
        self.max_hops = max_hops

    def ping(self, host: str) -> str:
        safe_host = shlex.quote(host)
        command = ['ping', '-c', str(self.max_hops), safe_host]
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr.decode("utf-8")}'
c
app = FastAPI()
ping_service = SafePing()

@app.get="/ping")
def ping(host: str):
    output = ping_service.ping(host)
    return {'status': 'completed', 'output': output}