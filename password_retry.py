# 程式:密碼確認
# 讓使用者重複輸入密碼,最多3次
# 輸入正確,印出'登入成功'
# 輸入錯誤,印出'密碼錯誤,還有_次機會"

#寫法1: num為輸入剩餘的機會
password = 'a123456'
num = 3 #輸入機會

while num >0:
	keyin = input('請輸入密碼')

	if keyin == password:
		print('登入成功')
		break
	else:
		num = num - 1 #輸入機會-1。此行也可以寫在while迴圈之下,不一定要放在else中
		print('密碼錯誤!')
		if num > 0: #還有輸入機會時,才會顯示此段
			print('剩下',num,'次機會')
		else: #沒有輸入機會時,顯示此段
			print('無法登入,請與客服聯絡')


#===寫法2: num為輸入的次數===
#password = 'a123456'
#num = 1 #輸入次數

# 密碼輸入機會3次
#while num <=3:
#	keyin = input('請輸入密碼:')
#
#	if keyin == password: #當使用者輸入內容input與密碼password符合
#		print('登入成功')
#		break #結束迴圈
#	else:
#		print('密碼錯誤!!') #當密碼不符,提示還有幾次機會
#
#		if num <3:
#			print('剩下',3-num, '次機會')
#			num= num + 1 #輸入次數+1
#		else:
#			print('你已錯誤輸入',num,'次,請與客服聯繫') 
#			break #結束迴圈,要不然num永遠>3會停不下來

