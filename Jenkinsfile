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
	stage('Create Application'){
		steps {
			sh """
       			. venv/bin/activate
        		cd djoinclient
				briefcase create
			"""
		}
	}
	stage('Build Application'){
		steps {
			sh """
       			. venv/bin/activate
        		cd djoinclient
				briefcase build
			"""
		}
	}
	stage('Build Package'){
		steps {
			sh """
       			. venv/bin/activate
        		cd djoinclient
				briefcase package
			"""
		}
	}
    }
}
