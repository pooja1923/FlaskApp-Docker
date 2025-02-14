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
                    bat "docker build -t %DOCKER_IMAGE_NAME%:%DOCKER_IMAGE_TAG% ."
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Start the Flask app in a Docker container
                    bat "docker run --rm -d -p 5000:5000 --name flask_test %DOCKER_IMAGE_NAME%:%DOCKER_IMAGE_TAG%"
                    
                    // Wait for the server to start
                    sleep(time: 10, unit: 'SECONDS')

                    // Run tests inside the Docker container
                    bat "docker exec flask_test python -m pytest tests/"

                    // Stop the Flask app container
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
                    // Authenticate with Docker Hub and push the image
                    withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
                        bat "docker push %DOCKER_IMAGE_NAME%:%DOCKER_IMAGE_TAG%"
                    }
                }
            }
        }
        stage('Deploy Application') {
            steps {
                script {
                    bat '''
                    docker stop flask-calculator || exit 0
                    docker rm flask-calculator || exit 0
                    docker pull %DOCKER_IMAGE_NAME%:%DOCKER_IMAGE_TAG%
                    docker run -d -p 5000:5000 --name flask-calculator %DOCKER_IMAGE_NAME%:%DOCKER_IMAGE_TAG%
                    '''
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
