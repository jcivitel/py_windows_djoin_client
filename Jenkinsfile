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
	stage('Build Debian Bookworm'){
		steps {
			sh """
       			. venv/bin/activate
        		cd djoinclient
				briefcase create debian:bookworm
			"""
		}
		steps {
			sh """
       			. venv/bin/activate
        		cd djoinclient
				briefcase build debian:bookworm
			"""
		}
		steps {
			sh """
       			. venv/bin/activate
        		cd djoinclient
				briefcase package debian:bookworm
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
		}
		steps {
			sh """
       			. venv/bin/activate
        		cd djoinclient
				briefcase build windows
			"""
		}
		steps {
			sh """
       			. venv/bin/activate
        		cd djoinclient
				briefcase package windows
			"""
		}
	}
    }
}
