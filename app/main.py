from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.ping_command = ['ping', '-c', '1']

    async def ping(self, host: str) -> dict:
        try:
            full_command = shlex.join([*self.ping_command, host])
            result = subprocess.run(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return {'status': 'success', 'output': result.stdout.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.stderr.decode('utf-8')}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping_instance.ping(host)