### Challenge: keyRSA

> nc 103.245.249.76 49160\
> Author: Cli3nt

Challenge này có 1 file đính kèm là file để thực thi mã khóa flag.

#### \* [enc.py](https://github.com/M4rv3l-M3tavers3/FPTUHACKINGCTF2022-/blob/main/Cryptography/keyRSA/enc.py)

### $Explain source code

Các bước mã hóa giống như một chall về RSA hay gặp.\
Đầu tiên, tác giả đã chọn hai số nguyên tố 512 bits nhân với nhau để có được n ở output. Lấy e = 65537...

```python
p, q = getPrime(512), getPrime(512)
n = p * q
e = 65537

msg = bytes_to_long(flag)

assert n > msg
ct = pow(msg,e,n)

phi = (p-1) * (q-1)
d = pow(e,-1,phi)
```

Khi chúng ta chạy câu lệnh netcat(nc) trên kali thì chúng ta nhận được như sau:
![Screenshot 2022-06-27 181724](https://user-images.githubusercontent.com/77691959/176108422-a66d7aa9-a59f-4e53-983d-9ca06cb8f3cc.png)

Nếu chọn 'y' thì tôi nhận được n, e, x

Theo như source code ta có:

```python
print(f'\nx = {p % (n // 2)}')
```

Nhưng vì (n // 2) quá lớn so với p nên khi chia dư thì kết quả nó vẫn là p\
==> x = p\
==> q = n // p

Tiếp theo chính là tìm d, chúng ta đều biết rằng d chính là 1 thành phần bí mật trong mã hóa RSA và mỗi một chuỗi mã hóa chỉ tồn tại duy nhất một giá trị d.

Ở đây chúng ta cần nhập vào một giá trị d khác gọi là user_d sao cho user_d phải khác với d, nhưng pow(ct, user_d) và pow(ct, d) phải đồng dư với nhau.

```python
if user_d != d:
    if pow(ct,user_d,n) == pow(ct,d,n):
        print(flag)
    else:
        print('Better luck next time !!')
        exit(0)
else:
    print("Sorry you can't use my key, or maybe our keys were similar this time, try again !!")
    exit(0)
```

Vì đây là chia dư cho n nên chúng ta có thể tìm được một tập hợp các giá trị của user_d. Và sau đây là một các giải quyết khá đơn giản, tập hợp đấy sẽ tồn tại một giá d và các đồng như của nó sao cho 2 số gần nhau nhất hơn kém nhau đúng bằng bội chung nhỏ nhất của (p-1) và (q-1).

```python
alpha = math.lcm(p-1, q-1)
value = d + alpha
```

Sau khi đã tìm đc đồng dư của d thì đấy chính là user_d chúng ta cần để có thể bypass qua điều kiện "if" bên trong và có được flag.

![Screenshot 2022-06-28 141822](https://user-images.githubusercontent.com/77691959/176117648-fffb2e6a-44c3-4496-8154-4f1ab31cd1d6.png)

### [Source code exploit](https://github.com/M4rv3l-M3tavers3/FPTUHACKINGCTF2022-/blob/main/Cryptography/keyRSA/solve.py)

### Flag: FPTUHacking{Y0u_kn0w_t0_CR34t3_y0ur_0wn_k3y!!!}
