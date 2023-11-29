pipeline {
    agent any
	parameters {
		choice(name: 'PLATFORM', choices: ['linux', 'windows', 'ios', 'android'], description: 'Pick a Platform')
	}
    stages {
		stage('Python Enviroment'){
			steps {
				sh """
					python3 -m venv venv
					chmod +x venv/bin/activate
				"""
			}
		}
		stage('Install Reqirements'){
			steps {
				sh """
					. venv/bin/activate
					pip install -r requirements.txt
				"""
			}
		}
		stage('Create Image'){
			steps {
				sh """
					. venv/bin/activate
					cd djoinclient
					briefcase create ${PLATFORM}
				"""
			}
		}
		stage('Build Image'){
			steps {
				sh """
					. venv/bin/activate
					cd djoinclient
					briefcase build ${PLATFORM}
				"""
			}
		}
		stage('Create Package'){
			steps {
				sh """
					. venv/bin/activate
					cd djoinclient
					briefcase package ${PLATFORM}
				"""
			}
		}
		stage('Tag and Upload'){
			steps {
				sh """
					
				"""
			}
		}
    }
	post{
	failure{
		sh """
			sleep 5
		"""
	}
	cleanup{
		cleanWs()
	}
}
