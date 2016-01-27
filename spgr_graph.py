import plotly.plotly as py
import plotly.graph_objs as go
import math

def wordsFromFile():
    words = {}
    with open("spgrordliste.txt", encoding='utf-8') as f:
        for x in range(8):
            r = f.readline()
            words_three = f.readline().strip('\n').replace(" ", "").lower().split(',')
            words_two = f.readline().strip('\n').replace(" ", "").lower().split(',')
            words_one = f.readline().strip('\n').replace(" ", "").lower().split(',')
            all_words = [words_one, words_two, words_three]

            for l in all_words:
                weight_number = (all_words.index(l) + 1)**2
                for i in l:
                    words[i] = (weight_number, r)
            f.readline()
    for keys, value in words.items():
        print (keys)
        print (value[0], value[1]) 
    return words

wordsFromFile()


def personWordsFromFile():
    persons = ["Sondre", "Monica", "Marie", "Henrik", "Petter", "Lars"]
    personWords = {}
    with open("spgrpersonord2.txt", encoding='utf-8') as f:
        for x in range(len(persons)):
            words = ""
            for y in range(4):
                words += f.readline().lower().strip('\n').strip()
            personWords[persons[x]]  = [word.replace(" ", "") for word in words.split(':')[1].split(',')]
            f.readline()
    return personWords

print (personWordsFromFile())

def polarToCart(r, t):
    return (r*math.cos(math.radians(t)), r*math.sin(math.radians(t)))

def cartToPolar(x, y):
    return (math.sqrt(x**2 + y**2), math.degrees(math.atan2(y,x)))

def returnPositionSize(words, personWords):
    total = [0, 0]
    wordcount = 0
    size = 0
    for word in personWords:
        polar = tuple(words[word])
        size += polar[0]
        cart = polarToCart(float(polar[0]), float(polar[1]))
        total[0] += cart[0]
        total[1] += cart[1]
        wordcount += 1
    return (size/wordcount, cartToPolar(total[0], total[1]))

def getPosAndSize(person):
        words = wordsFromFile()
        personWords = personWordsFromFile()[person]
        return returnPositionSize(words, personWords)

sizeScale = 200

Monica = go.Scatter(
            r = [getPosAndSize("Monica")[1][0], getPosAndSize("Monica")[1][0], getPosAndSize("Monica")[1][0], getPosAndSize("Monica")[1][0]],
            t = [getPosAndSize("Monica")[1][1], getPosAndSize("Monica")[1][1], getPosAndSize("Monica")[1][1], getPosAndSize("Monica")[1][1]],
            mode='markers',

                name='Monica',
                    marker=dict(
                            color='rgb(27,158,119)',
                                    size=sizeScale*getPosAndSize("Monica")[0],
                                            line=dict(
                                                        color='white'
                                                                ),
                                                                        opacity=0.7
                                                                            )
                    )
Henrik = go.Scatter(
            r = [getPosAndSize("Henrik")[1][0], getPosAndSize("Henrik")[1][0], getPosAndSize("Henrik")[1][0], getPosAndSize("Henrik")[1][0]],
            t = [getPosAndSize("Henrik")[1][1], getPosAndSize("Henrik")[1][1], getPosAndSize("Henrik")[1][1], getPosAndSize("Henrik")[1][1]],
            mode='markers',
                name='Henrik',
                    marker=dict(
                            color='rgb(217,95,2)',
                                    size=sizeScale*getPosAndSize("Henrik")[0],
                                            line=dict(
                                                        color='white'
                                                                ),
                                                                        opacity=0.7
                                                                            )
                    )
Lars = go.Scatter(
            r = [getPosAndSize("Lars")[1][0], getPosAndSize("Lars")[1][0], getPosAndSize("Lars")[1][0], getPosAndSize("Lars")[1][0]],
            t = [getPosAndSize("Lars")[1][1], getPosAndSize("Lars")[1][1], getPosAndSize("Lars")[1][1], getPosAndSize("Lars")[1][1]],
            mode='markers',
                name='Lars',
                    marker=dict(
                            color='rgb(117,112,179)',
                                    size=sizeScale*getPosAndSize("Lars")[0],
                                            line=dict(
                                                        color='white'
                                                                ),
                                                                        opacity=0.7
                                                                            )
                    )
Petter = go.Scatter(
            r = [getPosAndSize("Petter")[1][0], getPosAndSize("Petter")[1][0], getPosAndSize("Petter")[1][0], getPosAndSize("Petter")[1][0]],
            t = [getPosAndSize("Petter")[1][1], getPosAndSize("Petter")[1][1], getPosAndSize("Petter")[1][1], getPosAndSize("Petter")[1][1]],
            mode='markers',
                name='Petter',
                    marker=dict(
                            color='rgb(231,41,138)',
                                    size=sizeScale*getPosAndSize("Petter")[0],
                                            line=dict(
                                                        color='white'
                                                                ),
                                                                        opacity=0.7
                                                                            )
                    )
Marie = go.Scatter(
            r = [getPosAndSize("Marie")[1][0], getPosAndSize("Marie")[1][0], getPosAndSize("Marie")[1][0], getPosAndSize("Marie")[1][0]],
            t = [getPosAndSize("Marie")[1][1], getPosAndSize("Marie")[1][1], getPosAndSize("Marie")[1][1], getPosAndSize("Marie")[1][1]],
            mode='markers',
                name='Marie',
                    marker=dict(
                            color='rgb(102,166,30)',
                                    size=sizeScale*getPosAndSize("Marie")[0],
                                            line=dict(
                                                        color='white'
                                                                ),
                                                                        opacity=0.7
                                                                            )
                    )
Sondre = go.Scatter(
            r = [getPosAndSize("Sondre")[1][0], getPosAndSize("Sondre")[1][0], getPosAndSize("Sondre")[1][0], getPosAndSize("Sondre")[1][0]],
            t = [getPosAndSize("Sondre")[1][1], getPosAndSize("Sondre")[1][1], getPosAndSize("Sondre")[1][1], getPosAndSize("Sondre")[1][1]],
            mode='markers',
                name='Sondre',
                    marker=dict(
                            color='rgb(230,171,2)',
                                    size=sizeScale*getPosAndSize("Sondre")[0],
                                            line=dict(
                                                        color='white'
                                                                ),
                                                                        opacity=0.7
                                                                            )
                    )



Outer = go.Scatter(
            r = [162, 162, 162, 162],
            t = [180.0, 180.0, 180.0, 180.0],
            mode='markers',
                name=' ',
                    marker=dict(
                            color='rgb(255,255,255)',
                                    size=0*getPosAndSize("Sondre")[0],
                                            line=dict(
                                                        color='white'
                                                                ),
                                                                        opacity=0.7
                                                                            )
                    )


data = [Monica, Henrik, Lars, Petter, Marie, Sondre, Outer]
layout = go.Layout(
    title='SPGR Slutt - Gruppe 5',
        font=dict(
                size=15
                    ),
                        plot_bgcolor='rgb(223, 223, 223)',
                            angularaxis=dict(
                                    tickcolor='rgb(253,253,253)'
                                        )
                            )
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='spgr-polar-scatter-2')
