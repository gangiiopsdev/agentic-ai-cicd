from fastapi import FastAPI
import subprocess
def safe_git_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr)
# Example usage: safe_git_command(['git', 'pull'])

from fastapi import FastAPI
app = FastAPI()

@app.get("/safe-git")
def run_safe_git():
    command = ['git', 'pull']  # Ensure this command is trusted or validated
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'stderr': e.stderr}