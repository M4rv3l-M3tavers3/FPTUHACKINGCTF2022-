# PHP is Easy

- IP: http://103.245.249.76:49154/

```php
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

### Phân tích:
- Đọc source code có thể rõ ràng thấy đây là một challenge về PHP. Và đây là một vul của PHP về [PHP Loose Comparsion](https://owasp.org/www-pdf-archive/PHPMagicTricks-TypeJuggling.pdf) và [Magic hashes – PHP hash "collisions"](https://github.com/spaze/hashes).
- Tôi thấy giá trị GET Parameter `0ni0n` và được gán cho variable `$a`. 
- Tiếp đến, `isset ($a)` nghĩa là nếu `$a` tồn tại thì sẽ alert với điều kiện: 
  
  `a != "0gdVISQL8Cm" && $md52 == $md51`
- Check hash md5 của `0gdVIdSQL8Cm`: `0e366928091944678781059722345471`
- Nhận khi đọc được một bài về [PHP Juggling type and magic hashes](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md?fbclid=IwAR1I7iyNDj6xRrOTmHtIg67Q2ksMtGqJ3-SYsbdQm6dnJZaQajWfeiK7llY#php-juggling-type-and-magic-hashes), thì so sánh `==`(loose), chỉ cần so sánh giá trị hash thì luôn bằng nhau.
- Nên lấy `$a` = `QNKCDZO` có hash là `0e830400451993494058024219903391` đem ra so sánh với mã hash trong đoạn code => Thỏa mãn điều kiện. 
- Ta có payload: `http://103.245.249.76:49154/?0ni0n=QNKCDZO`

Wait a seconds...

![image](https://user-images.githubusercontent.com/93731698/176144711-e87cdbbe-aa47-48ab-b9ac-a8accc5d0279.png)


### Flag: `FPTUHACKING{Md5_bY_pAAs_eZ_H4_H4}`
