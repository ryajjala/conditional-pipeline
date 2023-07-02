pipeline {
    agent any
    
    stages {
        stage('checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('build package') {
            steps {
                script {
                    sh "zip -r deploy.zip calculator.py templates"
                }
            }
        }
        
        stage('deploy package') {
            steps {
                script {
                    sh "unzip -o deploy.zip"  // Replace '/path/to/deploy' with your desired deployment directory
                    sh "mkdir -p templates;cp calculator.html templates/"
                    sh "python3 calculator.py"
                }
            }
        }
    }
    
    post {
        always {
            script {
                def processId = sh(returnStdout: true, script: "pgrep gunicorn").trim()
                input message: 'Manual approval required to kill the gunicorn process. Proceed?', ok: 'Kill', submitter: 'admin'
                sh "kill $processId"
            }
        }
    }
}
