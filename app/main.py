from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'localhost']

    def execute(self, host: str, cmd: list):
        if host not in self.allowed_hosts:
            raise ValueError('Host not allowed')
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr}__

app = FastAPI()
safe_subprocess = SafeSubprocess()

@app.get("/ping")
def ping(host: str):
    response = safe_subprocess.execute(host, ['ping', host])
    return {'status': 'completed', 'response': response}