# TestForJenkins2

Набор из 8 минимальных мок-тестов для запуска из Jenkins. В отличие от первого репозитория, здесь нет разбиения на папки и не требуется переменная выбора набора.

```bash
python3 -m pip install -r requirements.txt
python3 run_mock_tests.py
```

Это pytest-тесты с декораторами и шагами Allure Framework. Результаты Allure сохраняются в `allure-results`; путь можно задать через `ALLURE_RESULTS_DIR`.

## Jenkins и TestOps

`Jenkinsfile` запускает тесты через `allurectl watch` и загружает результаты в TestOps. На Jenkins-агенте должен быть установлен `allurectl`, а в Jenkins необходимо создать Secret text credential с идентификатором `allure-token` и значением токена TestOps. Используются те же endpoint и project id, что и в примере: `https://nimaruichi.qameta.in` и проект `1`.
