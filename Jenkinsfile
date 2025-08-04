pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "visit_counter"
    }

    stages {
        stage ('Build'){
            steps{
                echo 'Building Docker images...'
                sh 'docker-compose build'
            }
        }
        stage('Run'){
            steps{
                echo'Running Containers...'
                sh 'docker-compose up -d'
            }
        }
        stage('Test'){
            steps{
                echo 'Testing visit counter...'
                sh '''
                  echo "Sending curl request to trigger counter..."
                  for i in {1..3};do
                     curl --fail http://localhost:5000/
                     done
                '''
            }
        }
    }

    post {
        always {
            echo'Cleaning up unused Docker resources...'
            sh 'docker system prune -f'
        }
        success{
            echo'Visit Counter deployed and tested successfully'
        }
        failure{
            echo'Something went wrong.'
        }
    }    
}