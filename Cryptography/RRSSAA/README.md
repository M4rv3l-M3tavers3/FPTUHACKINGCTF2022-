### RRSSAA

> Descriptons: John thinks using large prime helps to encrypt message

Challenge này có 2 file đính kèm, trong đó có 1 file để thực thi mã khóa flag, và một file là kết quả mã hóa.

#### \* [out.txt](https://github.com/M4rv3l-M3tavers3/FPTUHACKINGCTF2022-/blob/main/Cryptography/RRSSAA/output.txt)

#### \* [enc.py](https://github.com/M4rv3l-M3tavers3/FPTUHACKINGCTF2022-/blob/main/Cryptography/RRSSAA/enc.py)

### $Explain source code

Theo source code dùng để encrypt(enc.py) thì flag được chia thành 2 phần sau đó mã hóa từng phần.

```python
c1 = flag[:35].encode()
c2 = flag[35:].encode()
```

1. Ở phần một thì khác với lý thuyết về mã hóa RSA, tác giả đã chọn duy nhất một số nguyên tố 512 bits và mũ 4 lên để có được n1 ở output.txt.

```python
p1 = q1 = r1 = s1 = getPrime(512)
n1 = p1 * q1 * r1 * s1

msg1 = bytes_to_long(c1)
ct1 = pow(msg1, e, n1)
```

Nhưng theo như mã hóa RSA thì chỉ cần 2 số nguyên tố p và q. Vậy nên tôi nghĩ đến việc căn bậc 2 số n1 ấy để có được n1' ở dạng p \* q

Sau đó tôi dùng căn bậc 2 của n1, ct1 và e để decode trên web.

![Screenshot 2022-06-27 164733](https://user-images.githubusercontent.com/77691959/175913444-389c829f-ae55-40cf-a376-d2c5952fc709.png)

Thì đã có được nửa đầu của flag.

> FPTUHacking{Us3_0f_s1ngl3_pr1m3_4nd

2. Ở nửa sau tôi dùng RsaCtfTool để decode dữ liệu và có được nửa sau của flag.

![Screenshot 2022-06-27 174415](https://user-images.githubusercontent.com/77691959/175924185-d0ee1999-fa67-4d33-bd9b-d16f02f79f35.png)
![Screenshot 2022-06-27 174456](https://user-images.githubusercontent.com/77691959/175924189-735bf623-9b89-4e18-8c83-b5ab37f2be9e.png)

#### Flag: FPTUHacking{Us3_0f_s1ngl3_pr1m3_4nd_cl0se_prim3s_w3r3_w4st3_0f_c0mput3r_Cycl35}
