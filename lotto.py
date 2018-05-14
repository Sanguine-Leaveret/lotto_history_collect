import urllib2
import json

getLottoNumber = "http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=%d"

lotto_data = {
	1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 
	10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 
	18:0, 19:0, 20:0, 21:0, 22:0, 23:0, 24:0, 25:0, 
	26:0, 27:0, 28:0, 29:0, 30:0, 31:0, 32:0, 33:0, 
	34:0, 35:0, 36:0, 37:0, 38:0, 39:0, 40:0, 41:0, 
	42:0, 43:0, 44:0, 45:0
}

for drw in range(1,726):
	print "[+]DRW:%d"%drw
	data = json.loads(urllib2.urlopen(getLottoNumber%drw).read())
	lotto_data[data['drwtNo1']]+=1
	lotto_data[data['drwtNo2']]+=1
	lotto_data[data['drwtNo3']]+=1
	lotto_data[data['drwtNo4']]+=1
	lotto_data[data['drwtNo5']]+=1
	lotto_data[data['drwtNo6']]+=1
	lotto_data[data['bnusNo']]+=1
print lotto_data



