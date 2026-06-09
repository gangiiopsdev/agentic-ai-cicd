from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    if not host.isdigit():
        return 'Invalid input'
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout
class App:
    def __init__(self):
        self.app = FastAPI()
    async def home(self):
        return {"message": "Agentic Self-Healing Pipeline"}
    async def ping(self, host: str):
        try:
            return run_ping(host)
        except subprocess.CalledProcessError as e:
            return f'Ping failed with error: {e.stderr}'
app_instance = App().app