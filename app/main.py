from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    @staticmethod
def run_ping(host: str) -> dict:
        try:
            args = ['ping', shlex.quote(host)]
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService()
    return service.run_ping(host)