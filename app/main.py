from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        pass

    def ping(self, host: str):
        args = ['ping', '-c', '4', host]
        try:
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    return safe_ping.ping(host)