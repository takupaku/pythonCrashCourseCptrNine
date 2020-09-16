from collections import OrderedDict

glossarySec=OrderedDict()

glossarySec['list']='python list helps to store information in one variable'
glossarySec['tuple']='tuple is similar to list except the fact that it is immutable and one cannot alter the values but can insert new values'
glossarySec['slice']='slice is a concept within list where one can use some of its items only by using semicolon'
glossarySec['method']='method is like functions and python has such as title,strlen etc'
glossarySec['loop']='looping is a technique in python and python uses for,do while,while loops'
glossarySec['variable']='variable is like a pot that stores information in it'
glossarySec['indentation']='indentation is space and most programming language uses it for readability where python uses it in place of bracket'


for k,v in glossarySec.items():
    print("\nkey:"+k)
    print("value:"+v)