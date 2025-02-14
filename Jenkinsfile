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
                    // Run tests inside the Docker container
                    bat "docker run --rm ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} python -m pytest tests/"
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
                    // Log in to Docker Hub
                    bat "docker login -u ${DOCKER_HUB_CREDENTIALS_USR} -p ${DOCKER_HUB_CREDENTIALS_PSW}"

                    // Push Docker image to Docker Hub
                    bat "docker push ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}"
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
