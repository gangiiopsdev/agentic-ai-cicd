from fastapi import FastAPI
import subprocess
def safe_git_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr)
# Example usage: safe_git_command(['git', 'pull'])