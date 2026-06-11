from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        pass

    @staticmethod
def ping(host: str):
        # Safer implementation
        try:
            args = ['ping', '-c', '1', host]
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    safe_ping_instance = SafePing()
    return safe_ping_instance.ping(host)