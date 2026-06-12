from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str) -> str:
        # Sanitize the host input to prevent shell injection
        sanitized_host = shlex.quote(host)
        command = f"ping {sanitized_host}"
        subprocess.run(command, shell=False, check=True)
        return "completed"

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = SafePing.safe_ping(host)
    return {"status": result}