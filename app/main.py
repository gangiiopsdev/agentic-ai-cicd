from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Safe implementation using list instead of shell command
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
class PingRouter:
    def __init__(self):
        self.ping_service = PingService()

    @app.get("/ping")
def ping(host: str):
        if not host.isalnum():  # Basic validation to prevent injection
            raise HTTPException(status_code=400, detail="Invalid input")
        result = self.ping_service.ping(host)
        return {"status": "completed", "result": result}

app = FastAPI()
app.add_route("/ping", PingRouter().ping)