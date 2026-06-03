from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Validate input more strictly to avoid injection attacks
        if not host.replace('.', '').isalnum():
            raise ValueError('Invalid host name')
        command = ['ping', '-c', '1', host]
        subprocess.run(command, check=True)

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return SafeSubprocess.ping(host)