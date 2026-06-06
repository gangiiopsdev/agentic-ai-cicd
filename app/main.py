from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation without using shell=True
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class App:
    def __init__(self):
        self.app = FastAPI()
        self.app.add_api_route('/ping', self.ping)

    async def ping(self, host: str):
        # Call the safe function instead of using subprocess directly
        return {'status': 'completed', 'output': safe_ping(host)}

app = App().app