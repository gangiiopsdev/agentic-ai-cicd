from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str) -> None:
        # Safe implementation using list instead of string for the command
        args = ['ping', host]
        # Ensure the input is properly sanitized or avoid using user input directly
        if not isinstance(host, str) or not host.strip():
            raise ValueError('Invalid host input')
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/{country_name}")
def home(country_name: str):
    return {"message": "Agentic Self-Healing Pipeline", "country": country_name}

@app.get("/ping")
def ping(host: str):
    PingCommand.safe_ping(host)
    return {"status": "completed"}