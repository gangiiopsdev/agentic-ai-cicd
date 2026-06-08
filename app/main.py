from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        safe_host = self.sanitize_input(host)
        subprocess.call(['ping', safe_host])

    @staticmethod
def sanitize_input(input_str: str) -> str:
        # Implement input sanitization logic here
        return ''.join(char for char in input_str if char.isalnum() or char in ['.', '-'])

global_ping_service = PingService()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    global_ping_service.ping(host)
    return {"status": "completed"}