def dao_nguoi_chuoi(chuoi):
    return chuoi [::-1]
#Sử dụng hàm và in ra kết quả 
input_string = input("Mời nhập chuỗi cần đảo ngược: ")
print("Chuỗi cần đảo ngược là: ", dao_nguoi_chuoi(input_string))