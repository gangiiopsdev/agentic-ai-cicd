from fastapi import FastAPI
import subprocess
class SanitizedHost:
    def __init__(self, host: str):
        self.host = self._sanitize_host(host)

    @staticmethod
def _sanitize_host(host: str) -> str:
        return ''.join(filter(str.isalnum, host))

class PingService:
    def ping(self, host: SanitizedHost) -> dict:
        try:
            result = subprocess.run(['ping', host.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return {'host': host.host, 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'host': host.host, 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    sanitized_host = SanitizedHost(host)
    service = PingService()
    return service.ping(sanitized_host)