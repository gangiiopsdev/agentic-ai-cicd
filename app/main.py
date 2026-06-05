from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout}
class SafeApp(FastAPI):
    @app.get("/ping")
    def ping(self, host: str):
        return safe_ping(host)