from fastapi import FastAPI
import subprocess
import shlex
class CommandSanitizer:
    @staticmethod
def sanitize_command(command_parts):
        sanitized_parts = []
        for part in command_parts:
            sanitized_part = shlex.quote(part)
            sanitized_parts.append(sanitized_part)
        return ' '.join(sanitized_parts)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host.strip() == '':
        return {"status": "failed", "error": "Empty hostname provided"}
    sanitized_host = CommandSanitizer.sanitize_command([host])
    try:
        result = subprocess.run(f'ping -c 4 {sanitized_host}', capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}