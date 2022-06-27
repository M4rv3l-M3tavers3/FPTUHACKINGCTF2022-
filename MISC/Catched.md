# Catched

- Chúng ta có 1 file zip,sau khi unzip xong thì chúng ta có 1 mớ hỗn độn và bị đi vào bế tắc.
Chúng tôi thử “file” cái file được unzip ra xem nó là gì(và nó là định dạng của file system linux nên chúng tôi đã sử dụng “FTK imager” để đọc thông tin bên trong của nó)

![image](https://user-images.githubusercontent.com/95273832/175828481-eee6e6de-c263-4129-85c8-815044fa3d37.png)

- Chúng tôi tìm được 1 số file trống và 2 file có chứa dữ liệu:

![image](https://user-images.githubusercontent.com/95273832/175828473-4db1f6b8-1329-41b6-9a33-e574e668ffc1.png)

![image](https://user-images.githubusercontent.com/95273832/175828465-cb4e9cca-776c-424a-938a-9c54aa494679.png)

- Nhận ra được file mp3(cứ ngỡ là sẽ có flag rồi ,nhưng không,lại bế tắc tiếp khi nó thật sự như tiêu đề của nó”just a song”.lại bó tay tiếp và ngồi mò mẫm tìm  tool recover file khi chúng tôi thấy file kết thúc bằng “LAME 3.9..5” (là bộ mã hóa MPEG Audio Layer III (MP3) chất lượng cao) vì nghĩ rằng có thể nó đã bị mất mát dữ liệu trong quá trình encode(sai lầm  .-. .-.)

![image](https://user-images.githubusercontent.com/95273832/175828453-24310a50-83bd-4cb9-8041-752f435320ad.png)

- Thật bất ngờ khi chúng tôi cho nó vào hex editer,chúng tôi đã nhìn thấy “P.K” và “f.l.a.g.t.x.t”
và đã nhận ra đó là 1 file zip đã bị sửa,làm sai định dạng của file zip “PK”.Sau khi cắt nó sang 1 file hex khác thì chúng tôi nhận ra rằng file zip đã bị chèn bit “00” vào giữa 2 bit.và công cuộc cày cuốc ngồi xóa từng bit “00” bắt đầu.

![image](https://user-images.githubusercontent.com/95273832/175828449-0cf9d8cb-0c5a-4977-80eb-7546c7b975e2.png)

- Cũng có 1 vấn đề nhỏ là file zip này đã bị encode với mật khẩu.nhưng so easy ,chúng tôi đã crack được nó(https://linuxconfig.org/how-to-crack-zip-password-on-kali-linux)

![image](https://user-images.githubusercontent.com/95273832/175828441-eea4f1ef-c00c-403b-8961-98afdb7f4113.png)

![image](https://user-images.githubusercontent.com/95273832/175828436-8bb76bf4-a3fc-4895-8019-d0eae7e1eb1c.png)


### FLAG: `FPTUHacking{1265654407417514740_wouldn_t_you_say_there_s_a_light_in_the_darkest_moment}`
