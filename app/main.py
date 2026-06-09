from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Secure implementation using subprocess.run for safe argument passing
        args = ['ping', host]
        subprocess.run(args, check=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return SafeSubprocess.ping(host)