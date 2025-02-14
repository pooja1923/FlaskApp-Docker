pipeline {
    agent { label 'windows' } // Use a Windows agent for the pipeline

    environment {
        // Set environment variables (e.g., Docker Hub credentials)
        DOCKER_HUB_USERNAME = 'poojak19'
        DOCKER_HUB_PASSWORD = credentials('docker-hub-credentials')  // Jenkins credentials
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
                    // Build the Docker image using Windows-compatible commands
                    bat "docker build -t ${DOCKER_REGISTRY}/${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests inside the Docker container on Windows
                    bat """
                    docker run --rm -v %CD%:/app -w /app ${DOCKER_REGISTRY}/${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:latest powershell -Command "pytest tests/test_app.py"
                    """
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
                    // Log in to Docker Hub on Windows
                    bat """
                    docker login -u ${DOCKER_HUB_USERNAME} -p ${DOCKER_HUB_PASSWORD}
                    docker push ${DOCKER_REGISTRY}/${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:latest
                    """
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker images after the pipeline is finished
            bat 'docker system prune -f'
        }

        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
