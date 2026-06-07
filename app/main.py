from fastapi import FastAPI
import subprocess
class SafePing:
    def ping(self, host: str):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    return safe_ping.ping(host)