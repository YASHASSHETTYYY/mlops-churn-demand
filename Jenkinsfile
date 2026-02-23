pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Training') {
            steps {
                bat 'python train.py'
            }
        }

    }
}
