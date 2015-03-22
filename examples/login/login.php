<?php
error_reporting(0);

if (($_POST["username"] == "admin") && ($_POST["password"] == "bf")) 
    $valid = "Successful";
else 
    $error = "Denied";
?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Example &#8250; brutto.py</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
</head>

<body>

<?php echo $valid.$error; ?>
    <h1>Example brutto.py > login</h1>
    <form method="post" action="?">
            <input type="text" name="username" placeholder="Username" required="required"/>
            <input type="password" name="password" placeholder="Password" required="required"/>
        <input type="submit" value="Login &raquo;"/>
    </form>

</body>
</html>
