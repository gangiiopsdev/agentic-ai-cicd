from fastapi import FastAPI
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            # Validate and sanitize the input
            import re
            if not re.match(r'^[a-zA-Z0-9.-]+$', host):
                return {'status': 'failed', 'error': 'Invalid hostname'}
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return SafePing.ping(host)