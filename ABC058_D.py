from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="058"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc071_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  mod=10**9+7
  n,m=map(int,input().split())
  X=list(map(int,input().split()))
  Y=list(map(int,input().split()))
  xb=[(X[i+1]-X[i])*(i+1)*(n-i-1)%mod for i in range(n-1)]
  yb=[(Y[i+1]-Y[i])*(i+1)*(m-i-1)%mod for i in range(m-1)]
  print(sum(xb)*sum(yb)%mod)
  """ここから上にコードを記述"""

  print(test_case[__+1])