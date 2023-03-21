length = float(input("가로:"))
width = float(input("세로:"))
height = float(input("높이:"))
volume = width*height*length
print("박스의 부피는 ",volume,"입니다.")

total_length = width+height+length

if total_length <= 80:
    price = 5000
elif 80 < total_length and total_length <= 100:
    price = 8000
elif 100 < total_length and total_length <= 120:
    price = 10000
elif 120 < total_length and total_length <= 160:
    price = 13000
else:
    price = "배송 불가"
 
print("총 길이: ",total_length)
print("택배 요금: ", price)
