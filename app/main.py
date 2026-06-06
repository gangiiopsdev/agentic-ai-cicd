from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        sanitized_host = ''.join(c for c in host if c.isalnum() or c in ' .-')
        try:
            result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True, shell=False)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}

app = FastAPI()
app.add_api_route("/ping", PingService.ping, methods=["GET"])