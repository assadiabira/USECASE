node{
  stage ("Dev") {
    fileExists '/var/lib/jenkins/Usecase/inverse_liste.java'
  }
  stage ("Test"){
    sh "javac /var/lib/jenkins/Usecase/inverse_liste.java"
  } 	
	stage ("Deployment"){
    dir('/var/lib/jenkins/Usecase/') {
        // some block
      sh "java Inverse"
    } 
	}
}	
