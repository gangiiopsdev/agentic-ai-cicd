from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        try:
            # Validate the host input to prevent OS command injection
            if not host.isalnum() and '-' not in host:
                raise ValueError("Invalid host input")
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {
                "status": "completed",
                "output": result.stdout.decode()
            }
        except subprocess.CalledProcessError as e:
            return {
                "status": "failed",
                "error": str(e)
            }

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return SafeSubprocess.ping(host)