import requests

# pycharm setting > project interpreter > requests설치
# 글작성 경로를 변수로 지정한 뒤 requests.post에 변수 포함해서 글작성 시도
# 콘솔에 200뜨면서 작성된글의 url이 뜬다면 성공
# 참고 : 티스토리 api 문서 https://tistory.github.io/document-tistory-apis/apis/v1/post/write.html
# access_token 발급 방법 : http://www.webpaper.kr/show/96&page=1
# access_token발급 받을 때 callback url을 내 블로그 주소로 하면 편함.

upload_url = 'https://www.tistory.com/apis/post/write?access_token={acess_token}&blogName={blog_name}&title={title}&content={content}&visibility=0&tag={tag_name}'

print(upload_url)
response = requests.post(upload_url)
print(response.text)