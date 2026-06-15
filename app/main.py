from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class SecurityFastAPI(FastAPI):
    @app.get("/ping")
def ping(self, host: str):
    # Use the safe_ping function
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}
app = SecurityFastAPI()