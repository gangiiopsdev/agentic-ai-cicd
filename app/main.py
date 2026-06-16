from fastapi import FastAPI
import subprocess
generate_subprocess_cmd = {'ping': ['ping', '{host}']} # Define a safe command dictionary
cmd = generate_subprocess_cmd.get(host)
if cmd:
    try:
        subprocess.run(cmd, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
else:
    return {"error": "Invalid host"}