pipeline {
    agent any

    environment {
        // Set environment variables (e.g., Docker Hub credentials)
        DOCKER_HUB_USERNAME = 'poojak19'
        DOCKER_HUB_PASSWORD = credentials('docker-hub-credentials')  
        IMAGE_NAME = 'flask-calculator'
        DOCKER_REGISTRY = 'docker.io'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Pull the latest code from GitHub
               git branch: 'main', url: 'https://github.com/pooja1923/FlaskApp-Docker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    docker.build("${DOCKER_REGISTRY}/${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:latest")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests inside a Docker container
                    docker.image("${DOCKER_REGISTRY}/${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:latest").inside {
                        sh 'pytest tests/test_app.py'
                    }
                }
            }
        }

        stage('Push Image to Docker Hub') {
            when {
                // Only push the image if tests pass
                branch 'main'  // Adjust the branch if necessary
            }
            steps {
                script {
                    // Log in to Docker Hub
                    docker.withRegistry("https://${DOCKER_REGISTRY}", "${DOCKER_HUB_USERNAME}") {
                        // Push the image to Docker Hub
                        docker.image("${DOCKER_REGISTRY}/${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:latest").push()
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker images after the pipeline is finished
            sh 'docker system prune -f'
        }

        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
