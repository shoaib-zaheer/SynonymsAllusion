
| POS tag list|Grammer |EXAM |
|---|---|---|
|CC |coordinating conjunction|
|CD |cardinal digit
|DT |determiner
EX 	|existential| there (like: "there is" ... think of it like "there exists")
FW  |foreign word
IN  |preposition/subordinating conjunction
JJ  |adjective  |  'big'
JJR |adjective, comparative | 'bigger'
JJS |adjective, superlative | 'biggest'
LS 	|List marker          |  1)
MD 	|modal                | could, will
NN 	|noun, singular       |'desk'
NNS |noun plural          |desks'
NNP |proper noun, singular|'Harrison'
NNPS| proper noun, plural |'Americans'
PDT |predeterminer        |'all the kids'
POS |possessive ending    |parent's
PRP |personal pronoun     | I, he, she
PRP$| possessive pronoun  |  my, his, hers
RB 	|adverb    very,      |silently,
RBR |adverb, comparative  |  better
RBS |Adverb, superlative  |  best
RP 	|particle    give up
TO 	| | to go 'to' the store.
UH 	|interjection     |errrrrrrrm
VB 	|Verb, base form  | take
VBD |verb, past tense,| took
VBG |Verb, gerund/present participle | taking
VBN |verb, past participle | taken
VBP |verb, sing. present, non-3d | take
VBZ | verb, 3rd person sing. present | takes
WDT |wh-determiner         | which
WP 	|wh-pronoun            | who, what
WP$ |possessive wh-pronoun |   whose
WRB |wh-adverb             |  where, when

### Random font files
Put a text object for every font you have on another layer, add a text game property to all of them and name them something meaningful. Then add an empty to the point where you want the text to start. The letters will be spawned there. Lastly execute this script:
```doctest
import bge
import random

scene = bge.logic.getCurrentScene()
string = "string"
fontList = ["font1", "font2", "font3"]
empty = scene.objects["Empty"]

for character in string:
    font = fontList[random.randint(0,2)]
    object = scene.addObject(font,empty)
    object["Text"] = character
    empty.worldPosition.x = empty.worldPosition.x + 1
```
The variable string is the string you get from the user's input. The items in fontList are the names of the text objects on the separate layers. The object empty is of course your empty so you have to use its name.

Then you go through your string letter by letter and generate a random number. This number can't be higher than length of fontList, so in this example it's 0 to 2 (3 items). A random text object (the one you just generated, so in case of a 2 it's the object "font3") will be added at the empty's location, the object's text will be changed to the letter and the empty will be moved (you should of course adjust this movement for your needs) so that the next letter won't be added on top of the other one.

#### Simple way to display text on screen in Python?
Here's a pygame solution. Just pass the random letters and color to Font.render and then blit the returned surface. To center it I call the get_rect method of the txt surface and pass the center of the screen_rect as the center argument. Note that you can't choose a different color for each letter. To do that you would probably have to render several "one letter" surfaces and then combine them.

Epilepsy warning - The text was getting changed really quickly (each frame (30 fps)) and I wasn't sure if that could cause epileptic seizures, so I added a timer to update the text only every 10 frames. Be careful if you want to increase the update speed.
https://coderedirect.com/questions/225498/simple-way-to-display-text-on-screen-in-python
```doctest
import sys
from random import choice, randrange
from string import ascii_letters

import pygame as pg


def random_letters(n):
    """Pick n random letters."""
    return ''.join(choice(ascii_letters) for _ in range(n))


def main():
    info = pg.display.Info()
    screen = pg.display.set_mode((info.current_w, info.current_h), pg.FULLSCREEN)
    screen_rect = screen.get_rect()
    font = pg.font.Font(None, 45)
    clock = pg.time.Clock()
    color = (randrange(256), randrange(256), randrange(256))
    txt = font.render(random_letters(randrange(5, 21)), True, color)
    timer = 10
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    done = True

        timer -= 1
        # Update the text surface and color every 10 frames.
        if timer <= 0:
            timer = 10
            color = (randrange(256), randrange(256), randrange(256))
            txt = font.render(random_letters(randrange(5, 21)), True, color)

        screen.fill((30, 30, 30))
        screen.blit(txt, txt.get_rect(center=screen_rect.center))

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
```

