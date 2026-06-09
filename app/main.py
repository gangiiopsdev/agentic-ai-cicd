from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the input to ensure it only contains allowed characters
        if not host.isalnum():
            raise ValueError('Invalid host name')
        result = PingCommand.safe_ping(host)
        return {'status': 'completed', 'result': result}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}