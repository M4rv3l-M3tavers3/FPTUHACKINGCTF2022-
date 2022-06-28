# Welcome to FPTU Ethical Hackers Kingdom
> Description: Welcome to [FPTU Ethical Hackers Kingdom](http://103.245.249.76:49159/) , where King of Deception and his people are living!\
> Author: antoinenguyen_09
* Vào web bấm F12 xem thử và thấy có một comment.

```html
<!-- Hahaha, you guys are idiots! The key was move from FPTU Ethical Hackers Kingdom to /source by our king Antoine!-->
```

*  Vì thế mình vào xem /source code. 

``` html
const express = require('express');
const path = require('path');
const virtual_machine = require('vm');

const app = express();

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', function (req, res, next) {
  let output = '';
  const secret = req.query.secret + '';
  if (secret && secret.length < 190 && !/[^A-Za-z).(]/.test(secret)) {
    try {
      const key = virtual_machine.runInNewContext(secret, {}, { timeout: 100 });
      if (key === 1073) {
        output = Buffer.from(process.env.FLAG).toString('base64');
      } else {
        output = 'https://i.imgur.com/OQFcXZD.jpg';
      }
    } catch (e) {
      output = Buffer.from('https://youtu.be/HRwVb2xrNDw').toString('base64');
    }
  } else {
    output = Buffer.from('https://youtu.be/HRwVb2xrNDw').toString('base64');
  }
  res.render('index', { title: 'Welcome to FPTU Ethical Hackers Kingdom <3', output });
});

app.get('/source', function (req, res) {
  res.sendFile(path.join(__dirname, 'app.js'));
});

module.exports = app;
```
### $Explain
* Quan trọng ở đây là từ dòng 16 đến 22, đang lấy secret là chuỗi chúng ta nhập vào và thỏa mãn các điều kiện trong if.
* Có 2 điều kiện cần thỏa mãn là chuỗi nhập vào không được vượt quá 190 kí tự và chuỗi đó chỉ được chứa các kí tự A-Za-z).( 
* Sau khi đã vượt qua được đoạn kiểm tra đó thì chúng ta có key = virtual_machine.runInNewContext(secret, {}, { timeout: 100 }) có nghĩa là nó đang đối chiếu với đối tượng {}, biên dịch code trong secret được viết và chạy nó sau tất cả điều này sẽ trả về kết quả đầu ra lưu lại trong key.
* Sau đó nếu key bằng cả giá trị và kiểu với số 1073 thì chúng ta sẽ nhận được flag ở dạng base64
### $Solution
* Giống như console của trình duyệt chúng ta giờ nhập một chuỗi thỏa mãn được các điều kiện nhưng vẫn phải lấy được kiểu số 1073 để in ra được flag cuối cùng.
* Trong các kí tự có thể nhập để ý thấy chỉ có chữ và các kí hiệu khác như ).( không thấy có số mà ở đây cần lấy giá trị là kiểu số 1073 nên chúng ta sẽ nghĩ đến hàm length có sẵn trong javascript, và cũng không được có " nên chúng ta khó có thể tạo một chuỗi bình thường chĩnh vì vậy chúng ta nghĩ tới các kiểu chuỗi có sẵn như NaN, null, undefined, Infinity và thêm một lưu ý là chuỗi nhập vào không vượt quá 190 nên kết hợp với các hàm cộng và nhân giá trị với hàm length như concat và repeat để độ dài chuỗi có thể tăng lên nhanh chóng mà vẫn không vượt quá 190 kí tự.
* Ví dụ: Sau khi tính toán ta có phép toán đạt được 1073 mà vẫn có độ dài thỏa mãn là: 1073 = 9 * 9 * ( 4 + 9 ) + 3 + 8 + 9 , ta có tương ứng 9 = String().concat(undefined) sau đó 9 * 9 thêm vào là repeat(String().concat(undefined).length) và cứ tương tự như vậy.

``` console
String().concat(undefined).repeat(String().concat(undefined).length).repeat(String().concat(null).concat(undefined).length).concat(NaN).concat(Infinity).concat(undefined).length
```

* Flag ở dạng base64: RlBUVUhhY2tpbmd7YmFuX3F1YV9odSxiYW5fZGFfYmlfQW50b2luZV9uaG90X3Zhb19qc19qYWlsfQ== . Chuyển đổi về chuỗi.

![image](https://user-images.githubusercontent.com/95297205/175923543-b4205eb2-3a8b-430f-ac63-dfcde1b3a183.png)
 
### Flag: FPTUHacking{ban_qua_hu,ban_da_bi_Antoine_nhot_vao_js_jail}
                                   
