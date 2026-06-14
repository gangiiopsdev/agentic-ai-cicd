from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use subprocess safely by avoiding shell=True and using a list for the arguments.
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class SafeFastAPI(FastAPI):
    @app.get("/safe-ping")
    def safe_ping_endpoint(self, host: str):
        return safe_ping(host)

app = SafeFastAPI()