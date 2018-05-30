import sys,requests,json,random
def between_markers(text: str, begin: str, end: str):
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]

if __name__ == "__main__":
    items = sys.argv[1:]
    if len(items)>=3 :
        host_link = items[3] if len(items)==4 else "http://127.0.0.1:8000/"
        int_items = [int(items[i]) for i in range(3)]
        request = requests.get("https://randomuser.me/api/",
            params={'format':'json',
                    'results':int_items[0],
                    'inc':'login,email',
                    })
            # ,data={'results':options["how_many"]})
        results = json.loads(request.text).get("results")
        for user in results:
            s = requests.Session()
            s.get(host_link+'auth/')
            if 'csrftoken' in s.cookies:
                csrftoken = s.cookies['csrftoken']
                s.post(host_link+'sign_up/',
                data = {'username':user['login']['username'],
                        'password':user['login']['password'],
                        'conf-password':user['login']['password'],
                        'email':user['email'],
                        "csrfmiddlewaretoken":csrftoken
                        }
                )
            for post_i in range(int_items[1]):
                res = requests.get('https://jaspervdj.be/lorem-markdownum/markdown-html.html')
                content = between_markers(res.text,'<pre class="markdown">','</pre>')
                s.get(host_link+'posts_list/create/')
                if 'csrftoken' in s.cookies:
                    csrftoken = s.cookies['csrftoken']
                    s.post(host_link+"posts_list/create/", data = {
                    'title': [user['login']['username']+' Post'], 
                    'content': [content],
                    'image': [''], 
                    'publish_month': [random.randint(1, 12)], 
                    'publish_day': [random.randint(1, 28)], 
                    'publish_year': [random.randint(2000, 2018)],
                    "csrfmiddlewaretoken":csrftoken})
            res = s.get(host_link+'posts_list_json/')
            posts = json.loads(res.text)
            random.shuffle(posts)
            if len(posts)>int_items[2]:
                posts = posts[:int_items[2]+1]
            for like_post in posts:
                s.get(host_link+'add_like/'+str(like_post["slug"]))



        # print(len(results))
        # for i in results:
            
