pipeline {
    agent any

    environment {
        ALLURE_ENDPOINT = 'https://nimaruichi.qameta.in'
        ALLURE_PROJECT_ID = '1'
        ALLURE_RESULTS = 'allure-results'
        ALLURE_LAUNCH_NAME = 'TestForJenkins2'
        ALLURE_TOKEN = credentials('allure-token')
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh 'python3 -m pip install --user -r requirements.txt'
            }
        }

        stage('Run tests and upload to TestOps') {
            steps {
                sh '''#!/bin/sh
                    export PATH="$HOME/.local/bin:$PATH"
                    allurectl watch -- env ALLURE_RESULTS_DIR="$ALLURE_RESULTS" python3 run_mock_tests.py
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
        }
    }
}
