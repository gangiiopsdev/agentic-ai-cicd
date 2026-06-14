from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class SafePingFastAPI(FastAPI):
    @app.get('/ping')
    def ping(self, host: str):
        return run_ping(host)

app = SafePingFastAPI()