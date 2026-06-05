from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Sanitize the host input to prevent command injection
        safe_host = ''.join(filter(str.isalnum, host))
        try:
            output = subprocess.check_output(['ping', '-c', '1', safe_host], universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(host)