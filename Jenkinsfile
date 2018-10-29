node{
  stage ("Dev") {
    echo "Dev in progress"
    checkout scm
	}
  stage ("Test"){
		echo "Test in progress"
    when{
      sh "python -m py_compile /var/lib/jenkins/Usecase/jeu_plus_moins.py"
		  echo "code OK"
    }
  } 	
	//stage ("Deployment"){
		//sh "/var/lib/jenkins/Usecase/jeu_plus_moins.py"
		//junit "/var/lib/jenkins/Usecase/report.xml"
	//}
} 
   
		
