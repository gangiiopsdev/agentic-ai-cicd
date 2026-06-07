from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Sanitize the host input to avoid command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized_host = ''.join(filter(lambda x: x in allowed_chars, host))

    app = FastAPI()

    @app.get("/ping")
    def ping(sanitized_host: str):
        try:
            subprocess.run(['ping', sanitized_host], timeout=5, check=True, shell=False)
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
        except Exception as e:
            return {"status": "failed", "error": str(e)}

        return {"status": "completed"}