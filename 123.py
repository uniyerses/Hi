#得後題目之後要分析的是留言算平均長度(要宣告什麼變數)
#算出幾筆留言，思考答案要怎麼存下來(例如len/count)
#要算出每筆留言的長度個別為多少
#將個別留言的長度加起來(思考用什麼迴圈，例如wlile/for)
#計算平均長度=總留言長度/總留言筆數

#打開txt檔案當成一個資料夾
#把資料夾裡面的每一行印出來
#要先去掉/n這種多出來的空格
#把每一行字加到空字串裡面
#印出字串

#字串跑太多出來了，看一下字串列印到哪裡了

#不看全部留言，改看總共有多少筆留言好了
#求字串全部長度
#求第1筆跟第2筆留言看看
#第一筆留言就很長，那就來看一下全部留言的長度平均是多少

data = []

with open('n.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
print(data)