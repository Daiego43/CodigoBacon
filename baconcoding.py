#!/usr/bin/env python3
import sys
import os
import lorem


class BaconEncoding:
    __dicBacon = {'a': 'AAAAA', 'b': 'AAAAB', 'c': 'AAABA', 'd': 'AAABB', 'e': 'AABAA', 'f': 'AABAB', 'g': 'AABBA',
                'h': 'AABBB', 'i': 'ABAAA', 'k': 'ABAAB', 'l': 'ABABA', 'm': 'ABABB', 'n': 'ABBAA', 'o': 'ABBAB',
                'p': 'ABBBA', 'q': 'ABBBB', 'r': 'BAAAA', 's': 'BAAAB', 't': 'BAABA', 'u': 'BAABB', 'w': 'BABAA',
                'x': 'BABAB', 'y': 'BABBA', 'z': 'BABBB', 'j': 'BBAAA', 'v': 'BBAAB'}
    __dicBaconR = dict([(y, x) for x, y in __dicBacon.items()])

    def __montarLista(self, texto, message):
        l = []
        traducido = list(message)
        i = 0
        while i < len(texto) and traducido != []:
            if texto[i].isalpha():
                l.append([traducido.pop(0), texto[i]])
            else:
                l.append([texto[i], texto[i]])
            i += 1
        return l

    def phase1(self, message):
        """
        Recibe una cadena de caracteres,elimina los espacios y traduce todas las letras siguiendo el diccionario
        :param message:
        :return primera parte de la traduccion bacon:
        """
        original = str(message).lower()
        traduced = ''
        for letra in original:
            if letra.isalpha():
                traduced += self.__dicBacon[letra]
        return traduced

    def phase2(self, message, texto=""):
        '''
        Recibe una cadena ya encriptada y le asigna un "lorem ipsum"
        Las letras del lorem se ponen en mayusculas o minusculas segun sea A o B
        :param text:
        :param message:
        :return:
        '''
        if texto == "":
            texto = lorem.text()

        l = self.__montarLista(texto, message)
        fakemsg = ''
        for i in range(len(l)):
            if l[i][0] == 'A':
                fakemsg += l[i][1].lower()
            elif l[i][0] == 'B':
                fakemsg += l[i][1].upper()
            else:
                fakemsg += l[i][1]
        return fakemsg

    def __reversePhase1(self, message):
        bacon = ''
        l = ''
        for i in range(len(message)):
            l += message[i]
            if (i + 1) % 5 == 0:
                bacon += (self.__dicBaconR[l])
                l = ''
        return bacon

    def __reversePhase2(self, message):
        baconmessage = ''
        for letra in message:
            if letra.isalpha:
                if letra.islower():
                    baconmessage += 'A'
                elif letra.isupper():
                    baconmessage += 'B'
        return baconmessage

    def codificaBacon(self, message, fakemessage=""):
        return self.phase2(self.phase1(message), fakemessage)

    def decodificaBacon(self, message):
        return self.__reversePhase1(self.__reversePhase2(message))

    def alphalen(self, string):
        count = 0
        for char in string:
            if char.isalpha():
                count += 1
        return count
