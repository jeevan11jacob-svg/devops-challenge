pipeline {
    agent any

    environment {
        IMAGE_NAME = "jeevanjacob/devops-challenge"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements.txt
                    ./venv/bin/python -m pytest -v
                '''
            }
        }

        stage('Build & Push') {
            steps {
                echo 'Docker build and push will be configured with Jenkins credentials.'
            }
        }
    }
}
