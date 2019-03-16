# -*- coding: utf-8 -*-
from pprint import pprint 
import numpy as np
import unidecode
import webbrowser
import pyperclip
import pandas
import re

csv = pandas.read_csv("./masterSentences.csv", encoding='utf-16-le')

## all PinYin in sentences
msPinyins= []
for sentence in csv["Pronunciation2"]:
    for pronunciation in re.split(" |\.|\?", sentence):
        basePronunciation = unidecode.unidecode(pronunciation).lower()
        if basePronunciation != "" and basePronunciation not in msPinyins: 
            msPinyins.append(basePronunciation)


# all PinYin from PinYin Table
pinYinList = pandas.read_csv("./pinYinTable.csv", encoding='utf-16-le')

# pinyin coverage dict
masterInitialDict = {}
for initial in pinYinList.columns:
    masterInitialDict[initial] = 0
masterFinalDict = {}
for final in pinYinList.iloc[:,0]:
    masterFinalDict[final] = 0

# get finals and initials count
pinYinList.set_index('index', inplace=True)
for py in msPinyins:
    for word in pinYinList:
        r = pinYinList[word][pinYinList[word] == py]
        if not r.empty:
            initial = word
            final = r.index[0]
            masterFinalDict[final] = masterFinalDict[final] + 1
            masterInitialDict[initial] = masterInitialDict[initial] + 1

finalsNeverUsed = [k for k, v in masterFinalDict.items() if v == 0]
initialsNeverUsed = [k for k, v in masterInitialDict.items() if v == 0]


# print results
print("DONE: Finals you used : %i /%i (%f)"%(len(masterFinalDict.keys())-len(finalsNeverUsed), len(masterFinalDict.keys()), 100-len(finalsNeverUsed)*1.0/len(masterFinalDict.keys())*100))
print("Let's use Finals below!")
print(finalsNeverUsed)

print("\nDONE: Initials you used : %i /%i (%f)"%(len(masterInitialDict.keys())-len(initialsNeverUsed), len(masterInitialDict.keys()), 100-len(initialsNeverUsed)*1.0/len(masterInitialDict.keys())*100))
print("Let's use initials below!")
print(initialsNeverUsed)


print("===================")

sentences = ""
for sentence in csv["Chinese"]:
    sentences = "%s\n\n\n\n\n\n"%sentence

pyperclip.copy(sentences)
print("Copied senttences to your clipboard. Visit https://ttsmp3.com/ and convert above to MP3!!")
webbrowser.open('https://ttsmp3.com/')  # Go to example.com
