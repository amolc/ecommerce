import requests


def send_sms(
    number,
    body
):
    session = requests.Session()
    url = 'http://bhashsms.com/api/sendmsg.php?'
    params = {
        'user': 'success',
        'pass': 'sms@123',
        'sender': 'BHAINF',
        'phone': number,
        'text': body,
        'priority': 'ndnd',
        'stype': 'normal',
    }

    response = session.get(
        url,
        params=params
    )
    
    print(response)
