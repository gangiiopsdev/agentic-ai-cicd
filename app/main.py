from fastapi import FastAPI
import shlex
import subprocess
class SafePing:
    def __init__(self):
        pass

    def safe_ping(self, host: str) -> dict:
        try:
            args = ['ping'] + shlex.split(host)
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return {'status': 'success', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping_endpoint(host: str):
    return safe_ping_instance.safe_ping(host)