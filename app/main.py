from fastapi import FastAPI
import subprocess
class PingService:
    def ping(host: str):
        return subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService()
    try:
        result = service.ping(host)
        if result.returncode == 0:
            return {"status": "completed", "result": "success"}
        else:
            return {"status": "failed", "result": "failure"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}