# Piece Of Cake
> The original site was http://103.245.249.76:49155 but the site will likely be take down, the original file is:


```htm1
<?php 
include "flag.php"; 
highlight_file(__FILE__); 
error_reporting(0); 
$str1 = $_GET['0']; 

if(isset($_GET['0'])){ 
    if($str1 == md5($str1)){ 
        echo $onion1; 
    } 
    else{ 
        die(); 
    } 
} 
else{ 
    die();    
} 

$str2 = $_GET['1']; 
$str3 = $_GET['2']; 

if(isset($_GET['1']) && isset($_GET['2'])){ 
    if($str2 !== $str3){ 
        if(hash('md5', $salt . $str2) == hash('md5', $salt . $str3)){ 
            echo $onion2; 
        } 
        else{ 
            die(); 
        } 
    } 
    else{ 
        die(); 
    } 
} 
else{ 
    die();    
} 
?> 
```

### Strategy
- We can see that the file includes "flag.php", and gives us back two different flags if we meet the conditionals. As it turns out, we get back two parts of a single flag.
- I’ll break this blog post down into the two separate areas that we have to solve in order to get the flag. We can see that each one is passed in as a query parameter, because of `$_GET['0'], $_GET['1']` and so on.

### $Flag1
- This first part is as follows: 
```htm1
<?php 
include "flag.php"; 
highlight_file(__FILE__); 
error_reporting(0); 
$str1 = $_GET['0']; 

if(isset($_GET['0'])){ 
    if($str1 == md5($str1)){ 
        echo $onion1; 
    } 
    else{ 
        die(); 
    } 
} 
else{ 
    die();    
} 
```

- In short, we need to enter a string (as parameter “0”) where the md5 of the string is equivalent to the string itself.  Wait, what?
- That should be impossible (?), but the trick here is the == which is different than === (yes I know, computers are terrible).  PHP has two main comparison modes. The “loose” comparison mode, as shown on page 7 of [this presentation](https://owasp.org/www-pdf-archive/PHPMagicTricks-TypeJuggling.pdf), is easier for us to exploit.  Page 9 shows that if an operand “looks like” a number (for example, 0e12345), it will convert them and perform a numeric comparison. So, we’re looking for two strings that PHP will incorrectly interpret as numbers, specifically in scientific notation (“0e….").
- The md5 hash of `0e215962017` is `0e291242476940776845150308577824`, as seen [here](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md?fbclid=IwAR3a3sJnizCJZnrNVEqkcC-lVBeKdkIVZBmFkL7VWJ_MYdDKy6Rd715cdJs).
- So, if we plug in that string as our first parameter, we get the first part of our flag:

`http://103.245.249.76:49155/?0=0e1137126905`

![image](https://user-images.githubusercontent.com/93731698/175820279-6ddefd10-83ba-405d-a35e-72732ec86ded.png)

### $Flag2

Next up: 

```htm1
$str2 = $_GET['1']; 
$str3 = $_GET['2']; 

if(isset($_GET['1']) && isset($_GET['2'])){ 
    if($str2 !== $str3){ 
        if(hash('md5', $salt . $str2) == hash('md5', $salt . $str3)){ 
            echo $onion2; 
        } 
        else{ 
            die(); 
        } 
    } 
    else{ 
        die(); 
    } 
} 
else{ 
    die();    
```
- Another head-scratcher:  we need to find two parameters that are not equal to each other, yet when we hash a concatenation of a pre-determined salt, and the parameters, they equal each other.
- When I originally wrote the preceding sentence, I wrote “find two strings”… but that’s an assumption on my part.  We have to supply two parameters, they don’t need to be of type string.  In fact, we’ll get through this section by exploiting that assumption.
- You can try this code out at [writePHPonline](https://www.writephponline.com/):
```htm1
$salt = "something";
$str2[] = 1;
$str3[] = 2;

if ($str2 !== $str3) {
  echo "str2 is different from str3";
}

echo ($salt . $str2);
echo ($salt . $str3);
```
- If you run it, you’ll see that $str2 is considered different from $str3, so our first check passes.
- Then, when we concatenate a string with an array, the output is “somethingArray”.  Huh.  So PHP seems to be converting the array to the string “Array” and then concatenating it to the salt variable.
- That gives us our next bit of URL:
`http://103.245.249.76:49155/?0=0e1137126905&1[]=1&2[]=2`

![image](https://user-images.githubusercontent.com/93731698/175820568-c7c1d22c-f2fa-4987-84ee-61b0e342bfc7.png)

### $Flag:

![image](https://user-images.githubusercontent.com/93731698/175820756-96a99dcf-41c1-4483-8bb7-4c261b38f12f.png)

Flag: `FPTUHACKING{StR1Ngs_c0nCaTeNaT1oN_1s_EaSy_!!!}`

# References: 
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md?fbclid=IwAR3a3sJnizCJZnrNVEqkcC-lVBeKdkIVZBmFkL7VWJ_MYdDKy6Rd715cdJs, here will explain clearly `PHP Juggling type and magic hashes`.




