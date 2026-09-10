"""Produces one minimal Allure result for Jenkins/TestOps integration checks."""

import json
import os
import time
import uuid
from pathlib import Path


results_dir = Path(os.getenv("ALLURE_RESULTS_DIR", "allure-results"))
results_dir.mkdir(parents=True, exist_ok=True)
test_uuid = str(uuid.uuid4())
started = int(time.time() * 1000)

attachment = "api-health-log.txt"
(results_dir / attachment).write_text("Mock API health check: service is available.\n", encoding="utf-8")

result = {
    "uuid": test_uuid,
    "historyId": "mock-api-health",
    "testCaseId": "mock-api-health",
    "fullName": "MockApiTest.test_health",
    "name": "Mock API health test",
    "status": "passed",
    "stage": "finished",
    "start": started,
    "stop": started + 1,
    "attachments": [{"name": "mock log", "source": attachment, "type": "text/plain"}],
}
(results_dir / "api-health-result.json").write_text(json.dumps(result), encoding="utf-8")
print("Created API health Allure result")
