from fastapi import FastAPI
import re
import subprocess
class PingCommand:
    @staticmethod
def run(host: str):
        try:
            # Sanitize the host input using regex or similar methods to allow only valid IP addresses or domain names
            if not re.match(r'^[a-zA-Z0-9.-]+$', host):
                raise ValueError('Invalid host format')
            result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
            return result.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = PingCommand.run(host)
    return {"status": "completed", "output": output}