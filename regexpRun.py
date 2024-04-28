import  re
a='C|C++|Java|C#|Python|JavaScript'
# aa=re.findall('Python',a)
# print(aa)

# b='C0C|C++|Java8|C#9|Python6|JavaScript'
# bb=re.findall('\d',b)
# print(bb)



# c='83C72D1D8E67'
# cc=re.match('\d',c)
# print(cc.span())
# ccc = re.search('\d', c)
# print(ccc.group())
# cccc = re.findall('\d', c)
# print(cccc)

# d='83C72D1D8E67'
# def convert(value):
#     mathched=value.group()
#     if int(mathched)>=6:
#         return '9'
#     else:
#         return '0'
# dd = re.sub('\d', convert,d)
# print(dd)

# e='abc,acc,adc,aec,afc,ahc'
# ee=re.findall('a[cfd]c',e)
# print(ee)

# f='python1111pythojava678php'
# ff=re.findall('python',f)
# print(ff)

# g='python1111pythojava678php#\n\r'
# gg=re.findall('\W',g)
# print(gg)

# h = 'pythonpythonpythonpython'
# hh=re.findall('(python)*',h)
# print(hh)

# i='life is short,i use python,i love python'
# ii=re.search('life(.*)python(.*)python',i)
# print(ii.group())
# print(ii.group(0,1,2))
# print(ii.groups())