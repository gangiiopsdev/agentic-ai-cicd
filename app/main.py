from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str) -> str:
        # Sanitize the host input to prevent shell injection
        sanitized_host = shlex.quote(host)
        command = f"ping {sanitized_host}"
        process = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if process.returncode != 0:
            return "Error: " + str(error.decode('utf-8'))
        return "completed"

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = SafePing.safe_ping(host)
    return {"status": result}