pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'poojak19/flask-calculator'
        DOCKER_TAG = 'latest'
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
                    bat "docker build -t %DOCKER_IMAGE%:%DOCKER_TAG% ."
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat "docker run --rm -d -p 5000:5000 --name flask_test %DOCKER_IMAGE%:%DOCKER_TAG%"
                    sleep 10 
                    bat "pytest tests/"
                    bat "docker stop flask_test"
                }
            }
        }

        stage('Push Image to Docker Hub') {
            when {
                branch 'main'
            }
            steps {
                script {
                    withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
                        bat "docker push %DOCKER_IMAGE%:%DOCKER_TAG%"
                    }
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    bat '''
                    docker stop flask_calculator || exit 0
                    docker rm flask_calculator || exit 0
                    docker pull %DOCKER_IMAGE%:%DOCKER_TAG%
                    docker run -d -p 5000:5000 --name flask_calculator %DOCKER_IMAGE%:%DOCKER_TAG%
                    '''
                }
            }
        }
    }

    post {
        failure {
            echo "Build failed!"
            currentBuild.result = 'FAILURE'
        }

        success {
            echo "Build and deployment successful!"
        }
    }
}
