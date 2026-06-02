from fastapi import FastAPI
import subprocess
class PingHandler:
    def ping(self, host: str):
        # Safe implementation using subprocess.run
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    handler = PingHandler()
    return handler.ping(host)