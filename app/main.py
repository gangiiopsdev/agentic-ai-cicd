from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.command = ['ping', '{}']

    def run(self, host: str):  # Added a method that takes the host as an argument
        try:
            return subprocess.run(self.command.format(host), check=True, timeout=5)
        except subprocess.CalledProcessError as e:
            print(f'Ping failed: {e}')
            return None

app = FastAPI()
safe_ping_instance = SafePing()

@app.get('/ping')  # Fixed the URL path syntax error
async def ping(host: str):
    if safe_ping_instance.run(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}