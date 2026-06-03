from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

def ping(host: str):
    # Safe implementation
    response = SafePing.safe_ping(host)
    return {"status": "completed", "output": response}