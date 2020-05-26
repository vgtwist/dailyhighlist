import commonlib

def finviz_list(urltext):
	s = commonlib.urlget (urltext)
	s = s[s.find("chart.ashx"):]
	sym = []
	b = s.find("<br>")
	while b > 0:
		symbol = commonlib.extractstring(s[:b], "t=", 20, "\\")
		if symbol != None:
			sym.append (symbol)
		s = s[b+10:]
		s = s[s.find("chart.ashx"):]
		b = s.find("<br>")

	symbol = commonlib.extractstring(s[:b], "t=", 20, "\\")
	if symbol != None:
		sym.append (symbol)

	sym = list(set(sym))

	sym = list(filter(None, sym))
	return sym

def finviz_list_all (urltext):
	sym1 = finviz_list(urltext)
	sym2 = []
	if len(sym1) == 20:
		sym2 = finviz_list(urltext+"&r=21")

	sym = sym1 + sym2
	symbolstr = ",".join (sym)
	return symbolstr

resultstr = finviz_list_all("https://finviz.com/screener.ashx?v=111&s=ta_newhigh&f=fa_pe_profitable,sh_avgvol_o500")
print (resultstr)
commonlib.writestringtofile ("dailyhighlist.txt", resultstr)
