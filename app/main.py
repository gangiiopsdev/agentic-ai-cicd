from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host):
        if host.startswith('192.168.') or host.startswith('10.'):  # Example allowed IP ranges
            args = ['ping', host]
            result = subprocess.run(args, capture_output=True, text=True)
            return result.stdout
        else:
            raise ValueError('Invalid host for ping')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = PingCommand.safe_ping(host)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}