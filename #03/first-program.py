# Chương trình này sẽ hỏi một số thông tin cá nhân của bạn và in ra console.

print('Chào bạn hiền, tên cậu là gì?')
myName = input()
print('Tên bạn dài ' + str(len(myName)) + ' kí tự')
print('Bạn bao nhiêu tuổi vậy?')
myAge = input()
currentYear = 2020
print('Vậy là bạn sinh năm ' + str(currentYear - int(myAge)) + ' rồi.')
