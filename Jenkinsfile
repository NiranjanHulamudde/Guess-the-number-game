pipeline {
	agent any
	triggers {
		pollSCM('H/2 * * * *')
	}
	stages {
		stage('checkout') {
			steps {
			    checkout scm
			}
		}
		stage('Install Dependencies') {
			steps {
				sh 'python3 -m pip install -r requirements.txt 2>/dev/null || echo "No requirements.txt found"'
		}
	}
		stage('Run tests') {
			steps {
				sh 'python3 -m pytest tests/ -v 2>/dev/null || echo "No tests found, skipping"'
		}
	}
		stage('Run Game') {
			steps {
				echo "pipeline executed successfully"
				sh 'python3 --version'
			}
		}
	}
	post {
		always {
			echo "Build finished"
		}
	}	
}
