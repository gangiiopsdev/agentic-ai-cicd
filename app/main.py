from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        # Validate the input to prevent command injection
        if not self.is_valid_host(host):
            return {'error': 'Invalid host'}
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'output': result.stdout}

    def is_valid_host(self, host: str) -> bool:
        # Simple validation to allow only alphanumeric characters and periods
        return all(char.isalnum() or char == '.' for char in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    service = PingService()
    return service.ping(host)