from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use a list instead of a string for the command arguments
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class SafePing:
    @staticmethod
def main():
        app = FastAPI()

        @app.get("/")
        def home():
            return {"message": "Agentic Self-Healing Pipeline"}

        @app.get("/ping")
        def ping(host: str):
            # Sanitize input to prevent shell injection
            if not host.isalnum() and not all(char in '-.' for char in host):
                return {"error": "Invalid host name"}
            return safe_ping(host)
SafePing.main()