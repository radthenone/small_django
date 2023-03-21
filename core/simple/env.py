from pathlib import Path

import environ

# ENVIRONMENTS
env = environ.Env()

# PATHS
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent  # /core
PROJECT_DIR = BASE_DIR.parent  # /src
ENV_DIR = BASE_DIR.parent / ".envs"