from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        if not host.isalnum():
            raise ValueError('Invalid host name')
        # Use subprocess.run instead of subprocess.call for better control and security
        subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return SafeSubprocess.ping(host)