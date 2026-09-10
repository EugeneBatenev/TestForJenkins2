"""Entry point used by Jenkins to run the pytest + Allure mock tests."""

import os
import subprocess
import sys
from pathlib import Path


results_dir = os.getenv("ALLURE_RESULTS_DIR", "allure-results")
tests_dir = Path(__file__).parent / "tests"
raise SystemExit(subprocess.call([sys.executable, "-m", "pytest", str(tests_dir), f"--alluredir={results_dir}"]))
