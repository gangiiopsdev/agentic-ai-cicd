from fastapi import FastAPI
class PingService:
    def __init__(self):
        pass

    @staticmethod
def ping(host: str):
        try:
            # Sanitize the host input to prevent command injection
            sanitized_host = subprocess.list2cmdline([host])
            output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr}'

app = FastAPI()
group ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)