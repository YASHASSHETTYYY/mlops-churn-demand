pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '20'))
    }

    environment {
        PYTHONUNBUFFERED = '1'
        PIP_DISABLE_PIP_VERSION_CHECK = '1'
        PYTHONDONTWRITEBYTECODE = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python --version
                            python -m pip install --upgrade pip
                            python -m pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python --version
                            python -m pip install --upgrade pip
                            python -m pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            mkdir -p reports
                            python -m pytest -q --junitxml=reports/pytest.xml
                        '''
                    } else {
                        bat '''
                            if not exist reports mkdir reports
                            python -m pytest -q --junitxml=reports\\pytest.xml
                        '''
                    }
                }
            }
        }

        stage('Python Import Smoke Check') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python -c "import src.data_preprocessing, src.train_churn, src.train_demand, src.evaluate, src.predict"
                        '''
                    } else {
                        bat '''
                            python -c "import src.data_preprocessing, src.train_churn, src.train_demand, src.evaluate, src.predict"
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/pytest.xml'
            archiveArtifacts allowEmptyArchive: true, artifacts: 'reports/**'
        }
    }
}
