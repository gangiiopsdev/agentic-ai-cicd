from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    # Sanitize the host input
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(char in allowed_chars for char in host):
        return {'status': 'failed', 'error': 'Invalid characters in host'}

    app = FastAPI()

    @app.get="/ping")
    def ping(host: str):
        try:
            output = subprocess.check_output(['ping', safe_ping(host)], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

    return app