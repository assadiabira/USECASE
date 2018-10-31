#!/path/to/php
<?ph
$serveur= "mysql";
$db = "usecase";
$table = "famille_tbl";
// on se connecte à MySQL
$connect = new mysqli($serveur);
// on seléctionne la base
mysql_select_db($db);

// on crée la requete SQL
$sql = "SELECT nom,prenom,statut,DATE_FORMAT(date, '%d-%m-%Y') as datefr FROM famille_tbl";

// on envoie la requête
$req = mysql_query($sql) or die('Erreur SQL !<br>'.$sql.'<br>'.mysql_error());

// on fait une boucle qui va faire un tour pour chaque enregistrement
while($data = mysql_fetch_array($req))
    {
    // on affiche les informations de l'enregistrement en cours
    echo '<b>'.$data['nom'].' '.$data['prenom'].'</b> ('.$data['statut'].')';
    echo ' <i>date de naissance : '.$data['datefr'].'</i><br>';
    }

// on ferme la connexion à mysql
mysql_close();
?>
