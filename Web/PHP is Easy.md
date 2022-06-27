# PHP is Easy

- The original site was http://103.245.249.76:49154/ but the site will likely be take down, the original file is: 

```htm1
<?php
require "flag.php";
error_reporting(0);
 $md51 = md5( '0gdVIdSQL8Cm' ); 
 $a = @$_GET[ '0ni0n' ]; 
 $md52 = @md5($a); 
 if ( isset ($a)){ 
    if ($a != '0gdVIdSQL8Cm' && $md51 == $md52) { 
        echo "<script>alert('$flag')</script>"; 
    } else { 
        echo "0ni0n{F3k4_Fl4G}"; 
    } 
} 
show_source(__FILE__);
?>
```

### Strategy

- Tôi thấy file includes "flag.php" và biến đầu vào là `0ni0n` , mã hash md5 `0gdVIdSQL8Cm`. 
- Tôi phát hiện vulnerability của bài này nằm ở việc dùng operator `==`. Operator `===`, compare 2 variable chặt chẽ về kiểu dữ liệu và giá trị. Còn operator `==` thì chỉ xét về compare 2 variable có cùng value.
Example: “0ABC” sẽ bằng với “0dABC”.

- To exploit this vulnerability, i use intput hash MD5 stay [here](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md?fbclid=IwAR1I7iyNDj6xRrOTmHtIg67Q2ksMtGqJ3-SYsbdQm6dnJZaQajWfeiK7llY),
specifically i chose `0e215962017` to compare with hash MD5 ` gdVIdSQL8Cm`.

`http://103.245.249.76:49154/?0ni0n=0e215962017`

Wait a seconds...

![image](https://user-images.githubusercontent.com/93731698/175896148-3505ff75-f42a-4382-9240-04f2f7a68c2a.png)

### Flag: `FPTUHACKING{Md5_bY_pAAs_eZ_H4_H4}`
