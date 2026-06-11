from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate or sanitize the host input here
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}

    app = FastAPI()

    @app.get("/ping")
    def ping(host: str):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}

    return app