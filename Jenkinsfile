pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\shiva\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Training') {
            steps {
                bat '"C:\\Users\\shiva\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" train.py'
            }
        }

    }
}
