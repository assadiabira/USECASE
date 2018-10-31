node{
  stage ("Dev") {
    echo "Dev in progress"
    checkout scm
	}
  stage ("Test"){
    echo "Test in progress"
    sh "php -l /var/lib/jenkins/Usecase/consultation_mysql.php"
  } 	
	stage ("Deployment"){
		steps{
			sh "php -f /var/lib/jenkins/Usecase/consultation_mysql.php"
			archiveArtifacts artifacts: '/var/lib/jenkins/Usecase/archive.jar', fingerprint: true 
		}
	} 
} 
		
