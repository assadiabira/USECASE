node{
  stage ("Dev") {
    echo "Dev in progress"
    checkout scm
	}
  stage ("Test"){
    echo "Test in progress"
    sh "javac -g -Werror /var/lib/jenkins/Usecase/factorial_script.java"
		post{
			succes{
	 			echo "Code Ok"
			}
		}
  } 	
	stage ("Deployment"){
	sh "java /var/lib/jenkins/Usecase/factorial_script.java"
	junit "/var/lib/jenkins/Usecase/report.xml"
	}
} 
   
		
