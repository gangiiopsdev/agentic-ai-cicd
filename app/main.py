from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            # Using subprocess.Popen instead of subprocess.call for better security
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)