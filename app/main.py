from fastapi import FastAPI
class PingService:
    def ping(self, host: str):
        try:
            # Validate the host input
            if not self.is_valid_host(host):
                return {'status': 'error', 'message': 'Invalid host'}
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    def is_valid_host(self, host: str) -> bool:
        # Implement validation logic here
        return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)