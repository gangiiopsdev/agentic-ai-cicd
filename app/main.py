from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            # Validate and sanitize the input
            if not self.is_valid_host(host):
                raise ValueError("Invalid host")
            output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

    @staticmethod
def is_valid_host(host: str) -> bool:
        # Simple validation, replace with more robust logic as needed
        return all(c.isalnum() or c in ['.', '-', '_'] for c in host)

app = FastAPI()
class PingEndpoint:
    @staticmethod
def get(host: str):
        service = PingService()
        return service.ping(host)

@app.get("/ping")
def ping(host: str):
    endpoint = PingEndpoint()
    return endpoint.get(host)