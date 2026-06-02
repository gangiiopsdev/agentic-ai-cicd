from fastapi import FastAPI
import subprocess
def run_git_command(command):
    if not isinstance(command, str) or not command.strip().startswith('git '):
        raise ValueError("Invalid command")
    # Sanitize the input further by whitelisting allowed commands
    allowed_commands = ['git pull', 'git push', 'git status']
    if command not in allowed_commands:
        raise ValueError("Invalid command")
    return subprocess.run(command, shell=False, capture_output=True, text=True)