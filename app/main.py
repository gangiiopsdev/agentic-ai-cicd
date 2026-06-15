from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout
class SafeFastAPI(FastAPI):
    @get("/ping")
    def ping(self, host: str):
        status = safe_ping(host)
        return {'status': 'completed', 'output': status}
app = SafeFastAPI()