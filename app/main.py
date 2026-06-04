from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    result = subprocess.call(args)
    return result
class SafeApp(FastAPI):
    @app.get("/ping")
    def ping(self, host: str):
        return {'status': 'completed', 'result': safe_ping(host)}