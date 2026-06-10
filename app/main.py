from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    # Validate the host input
    if not validate_host(host):
        raise ValueError("Invalid host")
    result = subprocess.run(args, check=True, shell=False)
    return result.stdout

class PingService:
    def ping(self, host: str) -> dict:
        try:
            output = safe_ping(host)
            return {"status": "completed", "output": output}
        except ValueError as e:
            return {"status": "error", "message": str(e)}

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    return ping_service.ping(host)