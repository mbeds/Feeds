from pytrends.request import TrendReq
import plotly.express as px

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ['gold wanted', 'gold forsale', 'oil wanted','oil forsale']
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m')

#1 Interest over Time
data = pytrends.interest_over_time()
data = data.reset_index()

print(data)
fig = px.line(data, x="date", y=kw_list, title='Keyword Web Search Interest Over Time')
fig.show()
