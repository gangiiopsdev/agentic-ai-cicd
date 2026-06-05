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
            return f'Error: {e.stderr}'

app = FastAPI()
safe_subprocess = SafeSubprocess()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = host.strip().replace(' ', '')
    if len(safe_host) == 0 or not safe_host.isalnum():
        raise ValueError('Invalid host')
    response = safe_subprocess.execute(safe_host, ['ping', f'-c 4 {safe_host}'])
    return {'status': 'completed', 'response': response}