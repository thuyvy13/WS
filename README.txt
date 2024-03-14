
# [PTPM-XLDL-UDPM][SP24-BL2]Seminar Nhận diện nốt nhạc - Nhạc cụ Guitar



## Giới thiệu

- Giới thiệu về cách nhận diện nốt nhạc
- Thuật toán sử dụng
- Sử dụng phép biến đổi Fourier nhanh (FFT) để chuyển đổi tín hiệu âm thanh từ miền thời gian sang miền tần số
- Xử lý các nốt nhạc, tín hiệu dạng âm thanh
- Hướng dẫn thực hành và cài đặt

## Cài đặt

### Yêu cầu

- Python 3.x
- Các thư viện Python: `sounddevice`, `numpy`, `matplotlib`, `tkinter`

### Cài đặt thư viện

```bash
pip install sounddevice numpy matplotlib
```

### Chạy ứng dụng

```bash
python main.py
```

## Sử dụng

1. Chạy ứng dụng bằng cách thực thi file `main.py`.
2. Cửa sổ ứng dụng sẽ xuất hiện, hiển thị thông tin về âm thanh được ghi từ microphone và biểu đồ tần số tương ứng.
3. Nhấn nút "Stop/Continue" để tạm dừng hoặc tiếp tục ghi âm.
4. Đóng cửa sổ ứng dụng để kết thúc chương trình.

## Hình ảnh minh họa

![Screen 1](https://github.com/thuyvy13/Workshop-Seminar-Python-Identify-musical-notes---Guitar-musical-instruments/blob/main/screenshot/image.png)

![Screen 2](https://github.com/thuyvy13/Workshop-Seminar-Python-Identify-musical-notes---Guitar-musical-instruments/blob/main/screenshot/z5248748436494_6413d00323a05dcd06eaa6bd3812db20.jpg)

![Screen 3](https://github.com/thuyvy13/Workshop-Seminar-Python-Identify-musical-notes---Guitar-musical-instruments/blob/main/screenshot/z5248749332481_d05b0d4c09a5b996397e138d5a41dfb8.jpg)

## Tính năng

- Nhận dạng nốt nhạc dựa trên tần số của âm thanh.
- Hiển thị biểu đồ tần số của âm thanh trong thời gian thực.
- Khả năng tạm dừng và tiếp tục ghi âm từ microphone.

## Đóng góp

Nếu bạn có bất kỳ ý kiến đóng góp nào cho dự án này, vui lòng mở một issue hoặc gửi một pull request trên [GitHub repository](https://github.com/yourusername/real-time-note-detection).

## Tác giả

- Người tạo: [Your Name](https://github.com/yourusername)
- Email: your@email.com

## Giấy phép

Dự án này được phân phối dưới giấy phép [MIT License](https://opensource.org/licenses/MIT).

---

Hãy đảm bảo thay thế các phần như `yourusername`, `Your Name`, và `your@email.com` với thông tin của bạn. Đồng thời, đảm bảo cập nhật đường dẫn hình ảnh minh họa trong phần "Hình ảnh minh họa".
