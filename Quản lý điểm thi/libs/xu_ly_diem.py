import csv

def check_ma_hs(lstDT, mahs):
    for hs in lstDT:
        if hs.get('ma_hs') == mahs:
            return True
    return False 

def them_diem_thi(lstDT):
    try: 
        while True: 
            print('Nhap thong tin hoc sinh: ')
            ma_hs = ''
            while True:
                ma_hs = input('Ma hoc sinh: ')
                if check_ma_hs(lstDT, ma_hs):
                    print('=== Ma hoc sinh da ton tai ===\n')
                else:
                    break
            ngay_thi = input('Ngay thi: ')
            ho_ten_hs = input('Ho ten hoc sinh: ')
            mon_thi = input('Mon thi: ')
            diem_thi = float(input('Diem thi: '))
            ket_qua = input('Dau/Rot? (diem thi >= 5: Dau, nguoc lai: Rot ): ')
            hs_diem_thi = {'ma_hs':ma_hs, 'ngay_thi':ngay_thi, 'ho_ten_hs':ho_ten_hs, 
            'mon_thi':mon_thi, 'diem_thi':diem_thi,'ket_qua':ket_qua}
            lstDT.append(hs_diem_thi)
            n = input('Ban co muon tiep tuc? (1:TT): ')
            if n != 1:
                break
        return
    except Exception as er:
        print(er)

def in_ds_diem_thi(lstDT):
    try:
        print('{:8}{:20}{:12}{:10}{:10}{10}'.format('Ma HS','Ho ten',
        'Ngay thi','Mon thi','Diem thi','Ket qua'))
        for hs in lstDT:
            print('{:8}{:20}{:12}{:10}{:10}{10}'.format(hs['ma_hs'],
            hs['ho_ten_hs'],hs['ngay_thi'],hs['mon_thi'],hs['diem_thi'],hs['ket_qua']))
        return
    except Exception as er:
        print(er)

def in_diem_thi(hs):
    try:
        print('{:8}{:20}{:12}{:10}{:10}{10}'.format('Ma HS','Ho ten',
        'Ngay thi','Mon thi','Diem thi','Ket qua'))
        print('{:8}{:20}{:12}{:10}{:10}{10}'.format(hs['ma_hs'],
        hs['ho_ten_hs'],hs['ngay_thi'],hs['mon_thi'],hs['diem_thi'],hs['ket_qua']))
        return
    except Exception as er:
        print(er)

def tra_cuu_diem_thi(lstDT,MaHS):
    try:
        for hs in lstDT:
            if hS['ma_hs'] == MaHS:
                return hs
        return
    except Exception as er:
        print(er)

def xoa_diem_thi(lstDT,MaHS):
    try:
        for i in range(len(lstDT)):
            if lstDT[i]['ma_hs'] == MaHS:
                del(lstDT[i])
                return 1
        return 0
    except Exception as er:
        print(er)

# def thong_ke(lstHD):
#     try:
#        
#     except Exception as er:
#         print(er)   

def luu_file_csv(_path, lstDT):
    try:
        lstLuu = []
        lstLuu.append(['MaHS','HoTenHS','NgayThi','MonThi','DiemThi',
        'KetQua'])
        for hs in lstDT:
            lstLuu.append([hs['ma_hs'],hs['ho_ten_hs'],hs['ngay_thi'],hs['mon_thi'],hs['diem_thi'],hs['ket_qua']])
        f = open(_path,'w',newline='',encoding='utf-8')
        csv.writer(f).writerows(lstLuu)
        f.close()
        return 1
    except Exception as er:
        print(er)   

def doc_file(_path,lstDT):
    try:
        f = open(_path,'r', encoding='utf-8')
        for hs in csv.reader(f):
            if hs[0] == 'MaHS':
                continue
            hs_diem_thi = {'ma_hs':hs[0], 'ho_ten_hs':hs[1], 'ngay_thi':hs[2], 
            'mon_thi':hs[3], 'diem_thi':float(hs[4]), 'ket_qua':hs[5]}
            lstDT.append(hs_diem_thi)
        f.close()
        return
    except Exception as er:
        print(er)   
