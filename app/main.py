from fastapi import FastAPI
import subprocess
import shlex

class SafeHost:
    def __init__(self, host: str):
        self.host = shlex.quote(host)

    def get_safe_host(self) -> str:
        return self.host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = SafeHost(host).get_safe_host()
    try:
        result = subprocess.run(['ping', shlex.quote(safe_host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}