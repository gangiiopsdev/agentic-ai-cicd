from fastapi import FastAPI
import subprocess
class PingService:
    def execute_ping(self, host: str):
        try:
            # Validate and sanitize the input
            if not self.is_valid_host(host):
                raise ValueError('Invalid host provided')
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr}'

    def is_valid_host(self, host: str) -> bool:
        # Simple validation to ensure the host does not contain unexpected characters
        return all(c.isalnum() or c in ['.', '-'] for c in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    result = ping_service.execute_ping(host)
    return {"status": "completed", "result": result}