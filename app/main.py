from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        # Validate and sanitize input to mitigate command injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid hostname')
        escaped_host = subprocess.list2cmdline([host])
        return subprocess.call(['ping', escaped_host], capture_output=True, text=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):    result = PingCommand.safe_ping(host)
    return {'status': 'completed', 'output': result}