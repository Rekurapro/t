import requests
from re import findall
from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def generator():

    name = str(request.args.get('name'))

    url = 'http://name-generator.biz/ar/includes/generators/fancy.php?q='+name

    response = requests.get(url).text


    username1 = findall('''id="username1" value="(.*?)"''', response)[0]
    username2 = findall('''id="username2" value="(.*?)"''', response)[0]
    username4 = findall('''id="username4" value="(.*?)"''', response)[0]
    username6 = findall('''id="username6" value="(.*?)"''', response)[0]
    username7 = findall('''id="username7" value="(.*?)"''', response)[0]
    username8 = findall('''id="username8" value="(.*?)"''', response)[0]
    username9 = findall('''id="username9" value="(.*?)"''', response)[0]
    username10 = findall('''id="username10" value="(.*?)"''', response)[0]
    username12 = findall('''id="username12" value="(.*?)"''', response)[0]
    username13 = findall('''id="username13" value="(.*?)"''', response)[0]
    username14 = findall('''id="username14" value="(.*?)"''', response)[0]
    username15 = findall('''id="username15" value="(.*?)"''', response)[0]
    username16 = findall('''id="username16" value="(.*?)"''', response)[0]
    username17 = findall('''id="username17" value="(.*?)"''', response)[0]
    username18 = findall('''id="username18" value="(.*?)"''', response)[0]
    username19 = findall('''id="username19" value="(.*?)"''', response)[0]
    username5 = findall('''id="username5" value="(.*?)"''', response)[0]

    return (username1,username2,username4,username6,username7,username8,username9,username10,username12,username13,username14,username15,username16,username17,username18,username19,username5)
