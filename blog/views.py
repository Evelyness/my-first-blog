from django.shortcuts import render

# Create your views here.
def post_list(request):
    # 사용자가 보낸 HTTP 요청에 관련된 정보 
    return render(request, 'blog/post_list.html', {})