## Characters

> Description: FPTU security offers encryption for each character, is it worth?\
> Author: Cli3nt

Challenge này có 2 file đính kèm, trong đó có 1 file để thực thi mã khóa flag, và một file là kết quả mã hóa.

#### 1. [out.txt](https://github.com/M4rv3l-M3tavers3/FPTUHACKINGCTF2022-/blob/main/Cryptography/characters/out.txt)

#### 2. [enc.py](https://github.com/M4rv3l-M3tavers3/FPTUHACKINGCTF2022-/blob/main/Cryptography/characters/enc.py)

### $Explain source code

Trong output.txt tác giả cho một danh sách các ciphertext, n và e. Và từ enc.py thì ta biết rằng đây là mật mã [RSA](<https://en.wikipedia.org/wiki/RSA_(cryptosystem)>)

Phương thức mã hóa RSA trong chall này thì khá tương tự như lý thuyết về RSA. Như các chall về RSA hay gặp thì nó mã hóa hết message(plaintext) một lần và chỉ cho ra một dãy số output(ciphertext) tương ứng. Nhưng lần này ciphertext chính là một danh sách. Đọc trong source code tác giả cho thì thấy rằng code đã bị biến đổi để cho ra output(ciphertext) là một danh sách bằng cách encryp từng kí tự trong flag.

```python
ct = []
for i in flag:
    ct.append( pow(  bytes_to_long(i.encode()),e,n) )
```

### Solve:

Đầu tiên chúng ta sử dụng tool RsaCtfTool để thử xem có decode về thành dạng plaintext hay không?
![Screenshot 2022-06-27 145720](https://user-images.githubusercontent.com/77691959/175889749-0571df41-bd5f-4b61-baee-af865ab475cc.png)

Kết quả cho ra là chữ "F" chính là kí tự đầu của flag.

Vậy giờ ta chỉ cần dùng RsaCtfTool để decode từng kí tự một trong flag.\
![Screenshot 2022-06-27 151823](https://user-images.githubusercontent.com/77691959/175893302-4842deff-7ce0-4c69-a2e5-bfd0a60f3427.png)

Tôi đã code một đoạn scripts để encode từng kí tự bằng RsaCtfTool.

### [$Exploit code](https://github.com/M4rv3l-M3tavers3/FPTUHACKINGCTF2022-/blob/main/Cryptography/characters/solve.py)

### Flag: FPTUHacking{3ncRYpt1ng_34ch_ch4r_ainT_G0nn4_h3lp}
