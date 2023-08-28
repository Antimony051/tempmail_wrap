import requests
emails=["youremailhere@mailto.plus"]

semd_url="https://tempmail.plus/api/mails/"


def download_attachment(fname,id,mail,num): # to do, make this asynchronous, so that we can download multiple attachments in parallel
    get_data=f"https://tempmail.plus/api/mails/{id}/attachments/{num}?email={mail}"
    r = requests.get(url = get_data, params = {})
    with open(fname,"wb") as f:
        f.write(r.content)

def get_email(id,mail):
    email_url= f"https://tempmail.plus/api/mails/{id}?email={mail}"
    r = requests.get(url = email_url, params = {})

if __name__=="main":
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
# this module is a work in progress!!
