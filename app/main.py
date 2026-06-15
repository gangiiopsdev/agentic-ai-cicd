from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Validate and sanitize input to prevent code injection
    if not host.replace('.', '').replace('-', '').isalnum():
        raise ValueError('Invalid input')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class SafePingFastAPI(FastAPI):
    @app.get('/ping')
    def ping(self, host: str):
        return run_ping(host)

app = SafePingFastAPI()