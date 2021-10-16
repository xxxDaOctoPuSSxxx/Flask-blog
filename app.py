from flask import Flask, render_template
import random


app = Flask(__name__)
# list of cat images
images = [ "https://cdnimg.rg.ru/img/content/178/22/40/kotik_d_850.jpg",
    "https://n1s1.elle.ru/48/7b/36/487b36300c62c5f0cb905da52aa874b4/728x486_1_30b570c2f6c0da65bb56095068e05768@940x627_0xc0a839a4_18087198581488362059.jpeg",
    "https://n1s1.elle.ru/61/d0/31/61d0316c3140a72c9c6ce5eb25d683a3/728x523_1_27c8fc461e4f834154c49eab8e5ae4fc@1024x735_0xc0a839a4_7530263681488362272.jpeg",
    "https://n1s1.elle.ru/46/05/3c/46053c629a764f5f3d14b3d9eb6c1de1/728x728_1_1d0d63f12e5079044b04385f82408618@960x960_0xc0a839a4_10276838501488363185.jpeg",
    "https://n1s1.elle.ru/fe/48/ee/fe48ee77f9949718d1c1a11896d12891/728x485_1_9b07b06a9284f068c58297b360ae8b86@1024x682_0xc0a839a4_4452950441488363278.jpeg",
    "https://n1s1.elle.ru/74/66/3a/74663a1f6d78b58ca8cf6371321a410c/728x728_1_c1c72b63532cf2a47e1a178e03f69da3@1252x1252_0xc0a839a4_4877201821488363395.jpeg",
    "https://n1s1.elle.ru/c6/d2/1a/c6d21a0b72b64ca5035eb448a0ed3071/728x619_1_826be588b281558a057db23ae6cd9137@990x842_0xd42ee42a_12572696171425048969.jpeg",
    "https://n1s1.elle.ru/7b/21/05/7b2105ca4c748f7da6e6c76eeb685b12/728x621_1_3661dc3b6b63b66fd6d60d1e0512ab47@1280x1092_0xc0a839a4_345060981488362720.jpeg",
    "https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg",
    "https://cs11.pikabu.ru/post_img/2019/02/04/12/1549312329147951618.jpg",
    "https://cs9.pikabu.ru/post_img/2019/02/04/12/15493124851326424.jpg",
    "https://omoro.ru/wp-content/uploads/2019/08/prikolnye-kotiki-1.jpg" ]
@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)
if __name__ == "__main__":
    app.run(host="0.0.0.0")
