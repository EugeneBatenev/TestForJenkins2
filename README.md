# TestForJenkins2

Набор из 8 минимальных мок-тестов для запуска из Jenkins. В отличие от первого репозитория, здесь нет разбиения на папки и не требуется переменная выбора набора.

```bash
python3 -m pip install -r requirements.txt
python3 run_mock_tests.py
```

Это pytest-тесты с декораторами и шагами Allure Framework. Результаты Allure сохраняются в `allure-results`; путь можно задать через `ALLURE_RESULTS_DIR`.
