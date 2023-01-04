import requests
import string
import time

class MonsterPower():

    def __init__(self,url):
        self.url = url
    
    #private_method
    def __retornoApi(self):
        call = requests.get(self.url)
        call = call.json()
        return call

    def firstQuestion(self):
        dictionary_local = {}
        call = self.__retornoApi()

        for key,values in call.items():
            for object in values:
                for key in object:
                    if key == 'id' or key == 'name' or key == 'type' or key == 'atk' or key == 'def' or key == 'level' or key == 'race' or key == 'attribute':
                        dictionary_local[key] = object[key]
        return dictionary_local

    def secondQuestion(self):
        list_with_five_monsters = []
        dictionary_of_monster_local = {}
        call = self.__retornoApi()

        #Creating monster list
        for key,values in call.items():
            for object in values:
                if values.index(object) < 5:
                    auxiliary_dictionary = {}
                    for key in object:
                        if key == 'id' or key == 'name' or key == 'type' or key == 'atk' or key == 'def' or key == 'level' or key == 'attribute':
                            auxiliary_dictionary[key] = object[key]
                    list_with_five_monsters.append(auxiliary_dictionary)

        #Creating Json from monster
        dictionary_of_monster_local['data'] = list_with_five_monsters
        return dictionary_of_monster_local
    
    def thirdQuestion(self):
        list_with_five_monsters = []
        dictionary_of_monster_local = {}
        call = self.__retornoApi()
                
        #creating the monster list
        for key,values in call.items():
            for object in values:
                if "level" in object:
                    auxiliary_dictionary = {}
                    for key in object:
                        if key == 'id' or key == 'name' or key == 'type' or key == 'atk' or key == 'def' or key == 'level' or key == 'attribute':
                            auxiliary_dictionary[key] = object[key]
                    list_with_five_monsters.append(auxiliary_dictionary)

        #Sorting and creating the json
        list_with_five_monsters.sort(key=lambda k: k["level"])
        dictionary_of_monster_local['data'] = list_with_five_monsters
        return dictionary_of_monster_local
    
    def fourthQuestion(self):
        list_with_ten_monsters = []
        dictionary_of_monster_local = {}
        call = self.__retornoApi()
                
        #creating the monster list
        for key,values in call.items():
            for object in values:
                if values.index(object) < 10:
                    auxiliary_dictionary = {}
                    for key in object:
                        if key == 'id' or key == 'name' or key == 'type' or key == 'race':
                            auxiliary_dictionary[key] = object[key]
                    list_with_ten_monsters.append(auxiliary_dictionary)

        #creating the json 
        dictionary_of_monster_local['data'] = list_with_ten_monsters
        return dictionary_of_monster_local

    def fifthQuestion(self):
        dictionary_main = {}
        dictionary_of_monsters_local = {}
        list_of_monster = []
        counter = 0
        call = self.__retornoApi()

        #creating the monster list
        for key,values in call.items():
            for object in values:   
                if counter < 5: 
                    if 'atk' in object:
                        for key in object:
                            if key == 'atk' and object[key] > 3000: #checking object attack size
                                for link in object.get('card_images'):
                                    list_with_links_image = []
                                    dictionary_of_links_local = {}
                                    dictionary_of_links_local['image_url'] = link['image_url']
                                    dictionary_of_links_local['image_url_small'] = link['image_url_small']
                                    dictionary_of_links_local['image_url_croppped'] = link['image_url_croppped']
                                    counter +=1
                                    list_with_links_image.append(dictionary_of_links_local)
                                    dictionary_of_monsters_local[object['name']] = list_with_links_image
        #creating the json
        list_of_monster.append(dictionary_of_monsters_local)         
        dictionary_main['data'] = list_of_monster
        return dictionary_main

    def sixthQuestion(self):         
        list_with_filtered_monster = []
        dictionary_of_monster_local = {}
        call = self.__retornoApi()

        for key,values in call.items():
            for object in values:
                if "Magician" in object['name']:
                    if 'attribute' in object:
                        if object['attribute'] == 'DARK' and object['race'] == 'Spellcaster' and object['atk'] >= 2000 and object['level'] <= 8:
                            auxiliary_dictionary = {}
                            for key in object:
                                if key == 'id' or key == 'race' or key == 'atk' or key == 'type' or key == 'def' or key == 'level' or key == 'archetype' or key == 'attribute' or key == 'cards_sets' or key == 'card_images':
                                    auxiliary_dictionary[key] = object[key]
                                if key == 'name' or 'desc' in object and key == 'desc':
                                    mensagem = object[key].encode()
                                    auxiliary_dictionary[key] = mensagem
                            list_with_filtered_monster.append(auxiliary_dictionary)

        #creating the json 
        dictionary_of_monster_local['data'] = list_with_filtered_monster
        return dictionary_of_monster_local
    
    def seventhQuestion(self):
        list_with_filtered_monster = []
        dictionary_of_monster_local = {}
        call = self.__retornoApi()

        for key,values in call.items():
            for object in values:
                if "Magician" or "Dragon" or "Ancient" in object['name']:
                    # Solving Problem with Class<NoneType> in ATK
                    if 'atk' in object:
                        if 'type' and 'def' and 'level' and 'race' in object:
                            if type(object['atk']) is int and object['atk'] >= 4400 and object['type'] == 'Fusion Monster':
                                auxiliary_dictionary = {}
                                for key in object:
                                    if key == 'id':
                                        auxiliary_dictionary[key] = object[key]
                                    if key == 'name':
                                        mensagem = object[key].encode()
                                        auxiliary_dictionary[key] = mensagem
                                    if key == 'type':
                                        auxiliary_dictionary[key] = object[key]
                                    if key == 'atk':
                                        auxiliary_dictionary[key] = object[key]
                                    if key == 'def':
                                        auxiliary_dictionary[key] = object[key]
                                    if key == 'level':
                                        auxiliary_dictionary[key] = object[key]
                                    if key == 'race':
                                        auxiliary_dictionary[key] = object[key]
                                list_with_filtered_monster.append(auxiliary_dictionary)

            #creating the json 
            dictionary_of_monster_local['data'] = list_with_filtered_monster
            return dictionary_of_monster_local