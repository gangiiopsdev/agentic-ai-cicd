from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        # Secure implementation
        try:
            result = subprocess.run(['ping', '-c', '1', subprocess.check_output(['echo', host], text=True).strip()], capture_output=True, text=True)
            return {'status': 'success', 'output': result.stdout}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping_route(host: str):
    return ping_service.ping(host)