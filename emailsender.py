import requests
emails=["dfserdhgseserser@mailto.plus"]

semd_url="https://tempmail.plus/api/mails/"


def download_attachment(fname,id,mail,num): # to do, make this asincronoys, so that we can download multiple attachments in parallel
    get_data=f"https://tempmail.plus/api/mails/{id}/attachments/{num}?email={mail}"
    r = requests.get(url = get_data, params = {})
    with open(fname,"wb") as f:
        f.write(r.content)

def get_email(id,mail):
    email_url= f"https://tempmail.plus/api/mails/{id}?email={mail}"
    r = requests.get(url = email_url, params = {})


for email in emails:
    check_inbox= "https://tempmail.plus/api/mails?email="+email # check if email has arrived.

    r = requests.get(url = check_inbox, params = {})
    response = r.json()
    no_of_email=response["count"]

    if no_of_email > 0:
        for x in range(no_of_email):
            mail_id= response["mail_list"][x]["mail_id"]
            subject=response["mail_list"][x]["subject"]
    else:
        continue

# POST /api/mails/ HTTP/2
headers={"Host": 'tempmail.plus',
"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; rv":1"13.0) Gecko/20100101 Firefox/113.0',
"Accept": '*/*',
"Accept-Language": 'en-US,en;q=0.5',
"Accept-Encoding": 'gzip, deflate, br',
"Content-Type": 'multipart/form-data; boundary=---------------------------5184737432458306582398675661',
"Content-Length": '713',
"Referer": 'https":/"/tempmail.plus/en/',
"X-Requested-With": 'XMLHttpRequest',
"Origin": 'https":/"/tempmail.plus',
"DNT": '1',
"Sec-Fetch-Dest": 'empty',
"Sec-Fetch-Mode": 'cors',
"Sec-Fetch-Site": 'same-origin',
"Connection": 'keep-alive',
"Cookie": 'email=dfserdser%40mailto.plus; ezux_lpl_392527=1680073729352|01491bf5-f5f9-44b4-4e58-2c37522f6122|false',
"TE": 'trailers' }

body='-----------------------------5184737432458306582398675661\nContent-Disposition: form-data; name="email"\n\ndfserdhgseserser@mailto.plus\n-----------------------------5184737432458306582398675661\nContent-Disposition: form-data; name="to"\n\ndfserdser@mailto.plus\n-----------------------------5184737432458306582398675661\nContent-Disposition: form-data; name="subject"\n\nthis is the subject\n-----------------------------5184737432458306582398675661\nContent-Disposition: form-data; name="content_type"\n\ntext/html\n-----------------------------5184737432458306582398675661\nContent-Disposition: form-data; name="text"\n\nthis is the text body<br>\n-----------------------------5184737432458306582398675661--'

# -----------------------------5184737432458306582398675661
# Content-Disposition: form-data; name="email"
# dfserdhgseserser@mailto.plus
# -----------------------------5184737432458306582398675661
# Content-Disposition: form-data; name="to"
# dfserdser@mailto.plus
# -----------------------------5184737432458306582398675661
# Content-Disposition: form-data; name="subject"
# this is the subject
# -----------------------------5184737432458306582398675661
# Content-Disposition: form-data; name="content_type"
# text/html
# -----------------------------5184737432458306582398675661
# Content-Disposition: form-data; name="text"
# this is the text body<br>
# -----------------------------5184737432458306582398675661--


# -----------------------------4181726127412289611232222361
# Content-Disposition: form-data; name="email"
# dfserdhgseserser@mailto.plus
# -----------------------------4181726127412289611232222361
# Content-Disposition: form-data; name="to"
# dfserdser@mailto.plus
# -----------------------------4181726127412289611232222361
# Content-Disposition: form-data; name="subject"
# subject 1
# -----------------------------4181726127412289611232222361
# Content-Disposition: form-data; name="content_type"
# text/html
# -----------------------------4181726127412289611232222361
# Content-Disposition: form-data; name="text"
# text 1<br>
# -----------------------------4181726127412289611232222361--

# -----------------------------216060973541578475632918325083
# Content-Disposition: form-data; name="email"
# dfserdhgseserser@mailto.plus
# -----------------------------216060973541578475632918325083
# Content-Disposition: form-data; name="to"
# dfserdser@mailto.plus
# -----------------------------216060973541578475632918325083
# Content-Disposition: form-data; name="subject"
# sdfsdfsd
# -----------------------------216060973541578475632918325083
# Content-Disposition: form-data; name="content_type"
# text/html
# -----------------------------216060973541578475632918325083
# Content-Disposition: form-data; name="text"
# sdfsdf<br>
# -----------------------------216060973541578475632918325083--


# -----------------------------209659675221698408402131387713
# Content-Disposition: form-data; name="email"
# dfserdhgseserser@mailto.plus
# -----------------------------209659675221698408402131387713
# Content-Disposition: form-data; name="to"
# dfserdser@mailto.plus
# -----------------------------209659675221698408402131387713
# Content-Disposition: form-data; name="subject"
# 1
# -----------------------------209659675221698408402131387713
# Content-Disposition: form-data; name="content_type"
# text/html
# -----------------------------209659675221698408402131387713
# Content-Disposition: form-data; name="text"
# 1<br>
# -----------------------------209659675221698408402131387713--
