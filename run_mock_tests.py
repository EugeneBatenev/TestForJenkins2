"""Produces eight minimal Allure results for Jenkins/TestOps integration checks."""

import json
import os
import time
import uuid
from pathlib import Path


results_dir = Path(os.getenv("ALLURE_RESULTS_DIR", "allure-results"))
results_dir.mkdir(parents=True, exist_ok=True)
started = int(time.time() * 1000)

for number in range(1, 9):
    attachment = f"api-{number}-log.txt"
    (results_dir / attachment).write_text(f"Mock API check #{number} passed.\n", encoding="utf-8")
    result = {
        "uuid": str(uuid.uuid4()),
        "historyId": f"mock-api-{number}",
        "testCaseId": f"mock-api-{number}",
        "fullName": f"MockApiTest.test_check_{number}",
        "name": f"Mock API test #{number}",
        "status": "passed",
        "stage": "finished",
        "start": started + number,
        "stop": started + number + 1,
        "attachments": [{"name": "mock log", "source": attachment, "type": "text/plain"}],
    }
    (results_dir / f"api-{number}-result.json").write_text(json.dumps(result), encoding="utf-8")

print("Created 8 API Allure results")
