import urllib
import urllib2

def login_site_torrentRG():
   cookie = ""
   url = "https://www.torrentrg.com/bbs/login_check.php"
   login_form = {"mb_id":"erpyjune", "mb_password":"erpy000"}
   login_req = urllib.urlencode(login_form)
   request = urllib2.Request(url, login_req)
   response = urllib2.urlopen(request)
   cookie = response.headers.get('Set-Cookie')
   print "cookie ---"
   print cookie
   print "cookie ---"

def login_site_torrentUS():
   cookie = ""
   url = "http://www.torrentby.us/bbs/login_check.php"
   login_form = {"mb_id":"erpy", "mb_password":"erpy000"}
   login_req = urllib.urlencode(login_form)
   request = urllib2.Request(url, login_req)
   response = urllib2.urlopen(request)
   cookie = response.headers.get('Set-Cookie')
   print "cookie ---"
   print cookie
   print "cookie ---"

def login_site_Daum():
   cookie = ""
   url = "https://logins.daum.net/accounts/login.do"
   login_form = {"id":"erpyjune", "pw":"5softwise.co.kr", "slevel":"1", "weblogin":"1", "reloginSeq":"0", "url":"http://top.cafe.daum.net/"}
   login_req = urllib.urlencode(login_form)
   request = urllib2.Request(url, login_req)
   response = urllib2.urlopen(request)
   cookie = response.headers.get('Set-Cookie')
   print "cookie ---"
   print cookie
   print "cookie ---" 

def login_site_Daum2():
   user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
   user_referer = 'http://www.daum.net/'
   headers = { 'User-Agent':user_agent, 'Referer':user_referer }
   url = "https://logins.daum.net/accounts/login.do"
   login_form = {"id":"erpyjune", "inputPwd":"5softwise.co.kr", "slevel":"1", "weblogin":"1", "reloginSeq":"0", "url":"http://top.cafe.daum.net/", "ipSecurity":""}
   login_req = urllib.urlencode(login_form)
   request = urllib2.Request(url, login_req, headers)

   try:
      response = urllib2.urlopen(request)
   except urllib2.HTTPError as e:
      print 'Error code: ', e.code
   except URLError as e:
      print 'Except Reason: ', e.reason
   else:
      info = response.info()
      data = response.read()
      print data
      print "data ---" 
      print info
      print "info ---" 
      print 'code: ', response.code


def get_contentsRG():
   url = "http://www.site.com/somepage.php"
   request = urllib2.Request(url)
   request.add_header('cookie', cookie)
   response = urllib2.urlopen(request)
   data = response.read()

login_site_Daum2()

