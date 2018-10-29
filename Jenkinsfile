node{
  stage ("Dev") {
    echo "Dev in progress"
    checkout scm
  }
  stage ("Test"){
    sh ("/var/lib/jenkins/jeu_plus_moins_OK.py")
    if ("/var/lib/jenkins/jeu_plus_moins_OK.py" || true){
      echo ("code OK")
    }
  }  
} 
   
		
