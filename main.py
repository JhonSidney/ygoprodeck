import ygoprodeck
import os
from deep_translator import GoogleTranslator
import time

try:
    collections= [
        "https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Dark Magician",
        "https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Blue-Eyes White Dragon",
        "https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Red-Eyes Black Dragon"   
    ]

    #First_question
    list_of_monster = []
    dictionary_of_monster ={}
    for object in collections:
        monster =  ygoprodeck.MonsterPower(collections[collections.index(object)])
        list_of_monster.append(monster.firstQuestion())
    dictionary_of_monster['data'] = list_of_monster
    print("\nPRIMEIRA QUESTAO\n",dictionary_of_monster)

    #Second_question
    monster2 = ygoprodeck.MonsterPower("https://db.ygoprodeck.com/api/v7/cardinfo.php?race=aqua")
    print("\nSEGUNDA QUESTAO\n",monster2.secondQuestion())

    #Third_Question
    thirdQuestion = ygoprodeck.MonsterPower("https://db.ygoprodeck.com/api/v7/cardinfo.php?attribute=light&race=spellcaster")
    print("\nTERCEIRA QUESTAO\n",thirdQuestion.thirdQuestion())

    #Fourth_question
    fourthQuestion = ygoprodeck.MonsterPower("https://db.ygoprodeck.com/api/v7/cardinfo.php?type=spell%20card&race=ritual")
    print("\nQUARTA QUESTAO\n",fourthQuestion.fourthQuestion())

    #Fifth_Question
    fifthQuestion = ygoprodeck.MonsterPower("https://db.ygoprodeck.com/api/v7/cardinfo.php?type=Fusion Monster")
    print("\nQUINTA QUESTAO\n",fifthQuestion.fifthQuestion())

    #sixthQuestion
    sixthQuestion = ygoprodeck.MonsterPower("https://db.ygoprodeck.com/api/v7/cardinfo.php?")
    print("\n SEXTA QUESTAO\n",sixthQuestion.sixthQuestion())

    #SeventhQuestion
    seventhQuestion = ygoprodeck.MonsterPower("https://db.ygoprodeck.com/api/v7/cardinfo.php?")
    print("\n SETIMA QUESTAO\n",seventhQuestion.seventhQuestion())

except Exception as e:
    print("\n\n")
    message = " ".join(f"{e}".split())
    message = GoogleTranslator(source='en', target='pt').translate(message)
    print(f'FALHA DURANTE A REQUISICAO DA API YU-GUI-OH \n ERRO: {message}')
