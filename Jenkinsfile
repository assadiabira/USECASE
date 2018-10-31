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
		}
	// écriture d'un rapport 	
		post{
			always{
				junit "/var/lib/jenkins/Usecase/report.xml"
			}
			success{
				echo "code compilé"
			}
		}
	} 
} 
		
