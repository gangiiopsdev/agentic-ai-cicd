from fastapi import FastAPI
class PingService:
    @staticmethod
    def ping(host: str):
        # Sanitize the host input to prevent command injection
        safe_host = ''.join(filter(str.isalnum, host))
        try:
            result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    service = PingService()
    return service.ping(host)