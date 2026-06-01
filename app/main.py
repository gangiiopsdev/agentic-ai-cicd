from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Safely constructing the command without shell=True and validating input
        if not host or '&&' in host or ';' in host or '>' in host or '<' in host or '&' in host:
            raise ValueError('Invalid host input')
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = SafePing.safe_ping(host)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "failed", "error": str(e)}