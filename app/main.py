from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Validate input more strictly to avoid injection attacks
        import re
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host name')
        command = ['ping', '-c', '1', host]
        subprocess.run(command, check=True)

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return SafeSubprocess.ping(host)