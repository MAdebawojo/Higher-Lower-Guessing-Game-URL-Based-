from flask import Flask
from random import randint
app = Flask(__name__)

@app.route('/')
def my_home():
    return "<h1> Guess a number between 0 and 9</h1> " \
            "<img src='https://media0.giphy.com/media/3o7aCSPqXE5C6T8tBC/" \
            "giphy.gif?cid=ecf05e47omx26mvt8vp9er9v0j0ktjzkmz4xs0s5fepbkp6x&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"

def generate_number():
    return randint(0, 9)

@app.route('/<int:num>')
def random_number_check(num):
    rand = generate_number()
    # rand = 3 ##### this was used for testing
    print(rand)
    if num == rand:
        return "<h1 style='color: green'>You found me!</h1>" \
                "<img src='https://media2.giphy.com/media/l2Sq9qGTQnL5NyI6Y/200w.webp?c" \
               "id=ecf05e47t5czj22jbw9q9xte3mefde698unrgevlbf01rgqt&ep=v1_gifs_search&ri" \
               "d=200w.webp&ct=g' height='500px'>"
    elif num < rand:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
                "<img src='https://media3.giphy.com/media/Pn1gZzAY38kbm/200.webp?cid=" \
               "ecf05e47t5czj22jbw9q9xte3mefde698unrgevlbf01rgqt&ep=v1_gifs_search&rid=" \
               "200.webp&ct=g' height='500px'> "
    else:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
                "<img src='https://media0.giphy.com/media/VkIet63SWUJa0/200.webp?" \
               "cid=ecf05e47t5czj22jbw9q9xte3mefde698unrgevlbf01rgqt&ep=v1_gifs_search&" \
               "rid=200.webp&ct=g' height='500px'>"
