from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        if any(char not in allowed_chars for char in host):
            raise ValueError('Invalid characters in host name')
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = PingCommand.safe_ping(host)
        return {'status': 'completed', 'result': result}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}