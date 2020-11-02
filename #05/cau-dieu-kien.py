age = int(input('Nhập tuổi của bạn: '))

if age < 18:
    print('Em chưa 18')
elif age < 30:
    print('Chào thanh niên')
elif age < 40:
    print('Cháu chào chú')
elif age < 50:
    print('Cháu chào bác')
elif age < 80:
    print('Cháu chào cụ')
else:
    print('Chào bạn hiền')
