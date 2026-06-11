from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        # Secure implementation
        try:
            output = subprocess.check_output(['ping', '-c', '4', host], shell=False, universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)