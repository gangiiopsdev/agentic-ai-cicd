from fastapi import FastAPI
import subprocess
import shlex
def execute_safe_command(command_parts):
    try:
        safe_command = ' '.join(shlex.quote(arg) for arg in command_parts)
        result = subprocess.run(safe_command, capture_output=True, check=True, shell=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class FastAPIApp:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    def ping(self, host: str):
        command_parts = ["ping", shlex.quote(host)]
        result = execute_safe_command(command_parts)
        return {"status": "completed", "result": result}

if __name__ == "__main__":
    app_instance = FastAPIApp()
    import uvicorn
    uvicorn.run(app_instance.app, host="127.0.0.1", port=8000)