import pandas as pd
import webbrowser
from sel1 import mobile_names,prices
class table:

    def __init__(self,f):
        self.f=f
        html = f.to_html()
        text_file = open("index.html", "a+",encoding="utf-8")
        text_file.write(html)
        text_file.close()
        webbrowser.open("index.html")

df=pd.DataFrame({'name':['praveen','lathika','eashan','yuvan','praveen1','lathika1','eashan1','yuvan1','praveen2','lathika2'],
                 'age':[23,34,22,21,18,24,32,31,30,25],
                 'salary':[20000,30000,43000,12000,24000,25000,26000,27000,28000,27500]})
gf=pd.DataFrame({'name':['praveen','lathika','eashan','yuvan'],
                 'age':[35,30,5,3],
                 'occupation':['SE','Home Maker','Student','Student']})
cf=pd.DataFrame(columns=['mobile_name','price'])
cf['mobile_name']=mobile_names
cf['price']=prices
df1=table(df)
gf1=table(gf)
cf1=table(cf)