from fastapi import FastAPI
import subprocess
import shlex

class PingApp:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    def ping_endpoint(self, host: str):
        try:
            # Use subprocess.run for safe execution without shell=True
            result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = PingApp().app