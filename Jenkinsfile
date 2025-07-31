pipeline {
    agent any

    environment {
        IMAGE_NAME = "flood-risk-api"
    }

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/your-username/flood-risk-api.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest discover -s tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5050:5050 flood-risk-api'
            }
        }
    }
}
