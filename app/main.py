from fastapi import FastAPI
import subprocess
import shlex

class PingRequest:
    def __init__(self, host: str):
        self.host = host
        if not self.is_valid_host(self.host):
            raise ValueError("Invalid host")

    @staticmethod
def is_valid_host(host: str) -> bool:
        # Implement validation logic here, e.g., check for allowed characters or IP address format
        return True

app = FastAPI()

@app.post="/ping")
def ping_endpoint(request: PingRequest):
    args = ['ping', request.host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}