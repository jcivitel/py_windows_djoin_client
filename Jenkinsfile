pipeline {
    agent any
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
		stage('Build Linux'){
			steps {
				sh """
					. venv/bin/activate
					cd djoinclient
					briefcase create linux
				"""
				
				sh """
					. venv/bin/activate
					cd djoinclient
					briefcase build linux
				"""
				
				sh """
					. venv/bin/activate
					cd djoinclient
					briefcase package linux
				"""
			}
		}
		stage('Build Windows'){
			steps {
				sh """
					. venv/bin/activate
					cd djoinclient
					briefcase create windows
				"""
				
				sh """
					. venv/bin/activate
					cd djoinclient
					briefcase build windows
				"""
				
				sh """
					. venv/bin/activate
					cd djoinclient
					briefcase package windows
				"""
			}
		}
		stage('Move and Cleanup'){
			steps {
				sh """
					cleanWs()
				"""
			}
		}
    }
}
