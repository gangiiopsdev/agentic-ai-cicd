from fastapi import FastAPI
class SafePing:
    @staticmethod
    def ping(host: str):
        sanitized_host = subprocess.list2cmdline([host])
        try:
            result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.ping(host)