pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials') // Docker Hub credentials
        DOCKER_IMAGE_NAME = 'poojak19/flask-calculator' // Docker image name
        DOCKER_IMAGE_TAG = 'latest' // Docker image tag
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/pooja1923/FlaskApp-Docker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    bat "docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} ."
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat "docker run --rm -d -p 5000:5000 --name flask_test %DOCKER_IMAGE_NAME%:%DOCKER_IMAGE_TAG%"
                    sleep 10 // Wait for the server to start
                    bat "pytest tests/"
                    bat "docker stop flask_test"
                }
            }
        }

        stage('Push Image to Docker Hub') {
            when {
                expression {
                    // Only execute this stage if the previous stage (Run Tests) succeeded
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
               script {
                    withDockerRegistry([credentialsId: DOCKER_CREDENTIALS_ID, url: 'https://index.docker.io/v1/']) {
                        bat 'docker push %IMAGE_NAME%:%DOCKER_TAG%'
                    }
                }
            }
        }
    

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
