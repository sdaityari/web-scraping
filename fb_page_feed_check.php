<?php

session_start();

function check($message){
    $misleading = array(); //fill array for words to leave
    $keywords = array(); //fill array for words to search
    foreach ($misleading as $word){
        if (strpos(strtolower($message), $word))
	  return null;
    }
    foreach ($keywords as $word){
        if (strpos(strtolower($message), $word))
	  return $message;
	}
    return null;
}

function fetchUrl($url){

 $ch = curl_init();
 curl_setopt($ch, CURLOPT_URL, $url);
 curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
 curl_setopt($ch, CURLOPT_TIMEOUT, 20);
 // You may need to add the line below
 // curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,false);

 $feedData = curl_exec($ch);
 curl_close($ch); 

 return $feedData;

}

$limit = 1000;
//Retrieve auth token
//$authToken = fetchUrl("https://graph.facebook.com/oauth/access_token?type=client_cred&client_id=324750880918583&client_secret=7da2fbf8f4ed304db8eb8c0ae3682a17");

$token = $_SESSION['token'];

if (!$token){
    $token = $_GET['token'];
    $_SESSION['token'] = $token;
}

$page_id = ''; //fill id of fb page
//$url = "https://graph.facebook.com/331311713647609/posts?limit=$limit&access_token=$token";
$url = "https://graph.facebook.com/$page_id/posts?limit=$limit&access_token=$token";

//$json_object = fetchUrl("https://graph.facebook.com/{$profile_id}/feed?access_token={$authToken}");
$json_object = fetchUrl($url);

$feedarray = json_decode($json_object);

$messages = array();


?>

<html>
  <head>
    <title>Messages</title>
    <style>
    body{
      background-color:#B4AF91;
    }
    #container{
      width:960px;
      margin:0 auto;
    }
    .message{
      background-color:#787746;
      color:#cecece;
      margin: 10px;
      padding: 5px;
      border-radius:5px;
    }
    .message a, a:visited{
      text-decoration: none;
      color: #ababab;
    }
    </style>
  </head>
  <body>
    <div id = "container">
      <?php
	$j = 0;
        foreach ( $feedarray->data as $feed_data ){
          $messages[$j] = check("{$feed_data->message}");
          if ($messages[$j])
            echo "<div class = 'message'>".$messages[$j]."<br /><a target='_blank' href='".$feed_data->actions[0]->link."'>Click here for original post</a></div>";
	  $j++;
 	}
	if (!$json_object)
	{
	  echo "NO OBJECT RECEIVED";
	}
      ?>
GET TOKEN FROM: http://www.neosmart.de/social-media/facebook-wall/
<form action='' method=get>
<input type='text' name='token' />
<input type="submit">
</form>
    </div>
  </body>
</html>
