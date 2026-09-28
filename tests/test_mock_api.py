"""Eight simple API mock tests instrumented by Allure Framework."""

import allure
import pytest


@allure.feature("Jenkins mock tests")
@allure.story("API suite")
@allure.label("layer", "api")
@allure.title("API mock test #{number}")
@pytest.mark.parametrize("number", range(1, 9), ids=lambda number: f"api-{number}")
def test_api_check(number: int) -> None:
    with allure.step(f"Run mock API check #{number}"):
        actual = "available"
        expected = "available"
        allure.attach(f"Mock API check #{number} passed.", "mock log", allure.attachment_type.TEXT)

    with allure.step("Verify mock response"):
        assert actual == expected

@allure.feature("Jenkins mock tests")
@allure.story("API suite")
@allure.label("layer", "api")
@allure.title("API mock test #{number}")
@pytest.mark.parametrize("number", range(1, 9), ids=lambda number: f"api-{number}")
def  test_api_check2(number: int) -> None:
    with allure.step(f"Run mock API check #{number}"):
        actual = "available"
        expected = "available"
        allure.attach(f"Mock API check #{number} passed.", "mock log", allure.attachment_type.TEXT)

    with allure.step("Verify mock response"):
        assert actual == expected

@allure.feature("Jenkins mock tests")
@allure.story("API suite")
@allure.label("layer", "api")
@allure.title("API mock test #{number}")
@pytest.mark.parametrize("number", range(1, 9), ids=lambda number: f"api-{number}")
def test_api_check3(number: int) -> None:
    with allure.step(f"Run mock API check #{number}"):
        actual = "available"
        expected = "available"
        allure.attach(f"Mock API check #{number} passed.", "mock log", allure.attachment_type.TEXT)

    with allure.step("Verify mock response"):
        assert actual == expected
