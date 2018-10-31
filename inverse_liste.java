class Inverse 
{ 
   static void main(String[ ] args) 
   { /* inverse d'une suite de caractère dans un tableau par 
       permutation des deux extrêmes */ 
    char [ ] Tablecar ={'a','b','c','d','e','f'} ; 
    int i, j ; 
    System.out.println("tableau avant : " + String.valueOf(Tablecar)); 
    for ( i = 0 , j = 5 ;  i<j ; i++ , j-- ) 
     { char car ; 
       car = Tablecar[i]; 
       Tablecar[i ]= Tablecar[j]; 
       Tablecar[j] = car; 
     } 
    System.out.println("tableau après : " + String.valueOf(Tablecar)); 
  } 
}
