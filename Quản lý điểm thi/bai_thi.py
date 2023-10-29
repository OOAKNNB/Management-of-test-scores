from libs.xu_ly_diem import*
lstDiemThi = []
_path = 'file/dsdiemthi.csv'
print('CHƯƠNG TRÌNH QUẢN LÝ ĐIỂM THI THEO MÔN')

while True:
    print('''1: Đọc file điểm thi\n2: Thêm điểm thi\n3: Danh sách điểm thi\n4: Tra cứu điểm thi\n5: Xóa điểm thi\n6: Thống kê\n7: Lưu danh sách điểm thi ra file''')
    chon = int(input('Chọn chức năng cần thực hiện: '))
    if chon == 1:
        doc_file(_path,lstDiemThi)
        print('Đã đọc file vào lstDiemThi')
    elif chon == 2:
        them_diem_thi(lstDiemThi)
    elif chon == 3:
        in_ds_diem_thi(lstDiemThi)    
    elif chon == 4:
        mahs = input('Cho biết mã số học sinh: ')
        hs = tra_cuu_diem_thi(lstDiemThi, mahs)
        if hs == None:
            print('Không tìm thấy')
        else:
            in_diem_thi(hs)
    elif chon == 5:
        mahs = input('Cho biết mã học sinh: ')
        result = xoa_diem_thi(lstDiemThi, mahs)
        if result == 1:
            print('Đã xóa')
        else:
            print('Xóa không thành công')
    # elif chon == 6:
    elif chon == 7:
        result = luu_file_csv(_path,lstDiemThi)
        if result == 1:
            print('Đã lưu')
    else:
        break

    chon = input('Bạn có muốn tiếp tục không? (1: TT): ')
    if chon != '1':
        break