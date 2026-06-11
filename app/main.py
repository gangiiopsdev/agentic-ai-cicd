from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        if not self.validate_host(host):
            raise ValueError("Invalid host")
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

    def validate_host(self, host: str) -> bool:
        # Implement validation logic here
        return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService()
    response = service.ping(host)
    return {"status": "completed", "response": response}