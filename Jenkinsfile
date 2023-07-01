pipeline{
	agent any
	stages{
		stage('checkout'){
			steps{
				checkout scm
			}
		}
		stage('build package'){
			steps{
				script{
					sh " touch file1"
					sh "zip deploy.zip file1"
				}
			}
		}
		stage('deploy package'){
			steps{
				script{
					echo "deploy"
				}
			}
		}
	}
}