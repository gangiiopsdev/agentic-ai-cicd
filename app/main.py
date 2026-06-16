from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def safe_ping(host: str):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = PingService.safe_ping(host)
    return {"status": "completed", "output": result}