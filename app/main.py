from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        if self.validate_host(host):
            args = ['ping', host]
            subprocess.run(args, check=True)
        else:
            raise ValueError('Invalid host')

    def validate_host(self, host: str) -> bool:
        # Add validation logic here (e.g., regex to match allowed hostnames/IPs)
        return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    try:
        ping_service.ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}