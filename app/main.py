from fastapi import FastAPI
import subprocess
def get_output(cmd):\n    args = cmd.split()\n    result = subprocess.run(args, capture_output=True, text=True)\n    return result.stdout\n\napp = FastAPI()
\n@app.get("/")\ndef home():\n    return {"message": "Agentic Self-Healing Pipeline"}
\n@app.get("/ping")\ndef ping(host: str):\n    try:\n        output = get_output(f'ping {host}')\n        return {"status": "completed", "output": output}\n    except Exception as e:\n        return {"status": "error", "message": str(e)}