# -*- coding: utf-8 -*-
#티스토리 api 자동화 / 검수
import requests
import re
import json

g_client_id = 'ㅁㅂㅈㄷㅇㅁㅇㄹ' # 클라이언트 아이디
g_redirect_uri = 'ㄹㄷㅇㄾㅈㅅ' #리다이렉트 주소
g_user_id = 'ㄱㅈㅇ' #계정명
g_password ='ㅂㅁㅂㅎ' #비밀번호
blog_name = 'ㅂㄺㅇㄹ'#블로그이름
title = '제목' #글제목
content = '내용<br />내용'#글 내용
tag = '태그' #글 테그
result_url = '' #억세스 토큰 저장소

def login_token():
    global g_client_id, g_redirect_uri, g_user_id, g_password
    res = requests.get("https://www.tistory.com/oauth/authorize?client_id="+g_client_id+"&redirect_uri="+g_redirect_uri+"&response_type=token")
    kakao_cookie = res.headers['Set-Cookie'].replace("; path=/",'')    
    headers = {
        'Accept' : 'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'ko, en-US; q=0.8, en; q=0.6, zh-Hans-CN; q=0.4, zh-Hans; q=0.2',
        'Cache-Control' :  'no-cache',
        'Connection' : 'Keep-Alive',
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Cookie' : kakao_cookie,
        'Host' : 'www.tistory.com',
        'Referer' : res.url,
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    login_data = {
        'fp' : 'a668ac102f81b86f521c07dfb6dc992c',
        'keepLogin' : 'on',
        'loginId' : g_user_id,
        'password' : g_password,
        'redirectUrl' : res.url
        }       
    res = requests.post('https://www.tistory.com/auth/login', headers=headers, data=login_data)
    match = re.match('(.*?)access_token=(?P<access_token>.*?)&state=', res.url)
    gd = match.groupdict()
    access_token = gd['access_token'] #엑서스 토큰 발급
    return access_token

def test_insert(): #글쓰기   
    global blog_name, title, content, tag, result_url
    params = {
    'blogName' : blog_name,
    'title' : title,
    'content' : content,
    'tag' : tag,
    'category' : '0',
    'visibility' : '0',    
    'access_token' : login_token(),
    'output' : 'json'
    }
    data = json.dumps(params)
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    rd = requests.post('https://www.tistory.com/apis/post/write', data=data, headers=headers)
    if rd.status_code == 200:
        print(rd.status_code)              
        result_url = json.loads(rd.text)['tistory']['url']
        assert True
    else:
        print(rd.status_code)
        print(rd.text)
        item = json.loads(rd.text)
        print(rd.status_code)
        print(item["tistory"]["error_message"])
        assert False
        
def test_check():     #글쓴 내용 체크
    global blog_name, result_url, title, content, tag
    res = requests.get("https://www.tistory.com/apis/post/read?access_token="+login_token()+"&blogName="+blog_name+"&postId="+result_url.split('/')[3])
    ffw = lambda z, x : z[z.find("<"+x+">")+len(x)+2:z.find("</"+x+">")]
    assert title == ffw(res.text, 'title')
    assert content == ffw(res.text, 'content')
    assert tag== ffw(res.text, 'tag')    