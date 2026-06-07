from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        # Secure implementation
        if self.is_safe_host(host):
            subprocess.call(["ping", host])
        else:
            raise ValueError("Unsafe host")

def is_safe_host(host: str) -> bool:
    # Implement logic to validate the host, e.g., allow only certain IP ranges or domains
    return True

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    service = PingService()
    service.ping(host)
    return {"status": "completed"}