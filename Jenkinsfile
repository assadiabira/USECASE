node{
  stage ("Dev") {
    echo "Dev in progress"
    checkout scm
  }
  stage ("Test"){
    environment{
      code = "/var/lib/jenkins/jeu_plus_moins_OK.py"
    }
    sh ("code")
    if ( code || true){
      echo ("code OK")
    }
  }  
} 
   
		
