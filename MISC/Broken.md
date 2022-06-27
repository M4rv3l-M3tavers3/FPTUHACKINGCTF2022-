# Broken

- Chúng ta có 1 file ảnh PNG không thể mớ được
Sau khi dùng “exiftool” và hex “editer” để chắc chắn nó là 1 file PNG và nó đã bị sửa trở nên lộn sộn
- Mình đã thử sửa header của nó nhưng vẫn không mở được.khá là bế tắc,nhưng sau đó mình để ý đến các byte height và weight của nó thì thấy có vẻ không ổn(tất cả các byte = 0)

![image](https://user-images.githubusercontent.com/95273832/175828081-52907656-8ab6-4044-b6a6-ec91d312fb55.png)

- Ban đầu mình đã cố gắng chỉnh thủ công bằng việc tăng giá trị của height và weight nhưng đều không được ,đoạn này mình bị stuck rất là lâu.

- Sau khi tìm hiểu thêm về file PNG thì mình biết thêm là Height x Weight phải nhỏ hơn size của file ảnh. Lúc này mình đã nghĩ tới brute force ảnh để tìm được width và length thích hợp. Lục lọi mò mẫm khắp trên google thì mình cũng tìm được 1 đoạn code python để tìm ra size tương ứng cho bức ảnh :>

![image](https://user-images.githubusercontent.com/95273832/175828121-89f512c2-b210-42f9-8535-9769fb106e86.png)



Ohohohohoh,chỉnh hex và nhận flag thôi

![image](https://user-images.githubusercontent.com/95273832/175828139-6c398227-819e-4b61-87e6-7f43c5d13f76.png)

![image](https://user-images.githubusercontent.com/95273832/175828147-2c3880cf-9031-42ef-97cf-238d04813709.png)


# FLAG: `FPTUHacking{ju5t_ba5s1c_1HdR_r1ght}`
