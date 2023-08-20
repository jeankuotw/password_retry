# 小程式:密碼確認

password = 'a123456'
num = 1 #輸入次數

# 密碼輸入機會3次
while num >= 1 and num < 4:
	keyin = input('請輸入密碼(最多輸入3次):')
	if keyin == password: #當使用者輸入內容input與密碼password符合
		print('登入成功')
		break #結束迴圈
	else:
		print('密碼錯誤,還剩下', 3-num, '次機會') #當密碼不符,提示還有幾次機會
		num= num + 1 #輸入次數+1

# 密碼錯誤輸入超過3次時
while num >3 :
	print('你已錯誤輸入',num-1,'次,無法登入') #程式到此行num=4,所以需-1,告知錯誤輸入的次數
	break #結束迴圈,要不然num永遠>3會停不下來


