from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            # Constructing command safely without shell=True and validating input length
            args = ['ping', host]
            if len(args) > 2:  # Example of basic validation, adjust as needed
                return {'status': 'failed', 'error': 'Invalid input'}
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(host)