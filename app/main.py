from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class PingRouter(FastAPI):
    @app.get("/ping")
    def ping(self, host: str):
        # Call the safe_ping function instead of subprocess.call
        return {'status': 'completed', 'output': safe_ping(host)}