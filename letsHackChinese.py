# -*- coding: utf-8 -*-
from pprint import pprint 
import numpy as np
import unidecode
import webbrowser
import pyperclip
import pandas
import re

csv = pandas.read_csv("./masterSentences.csv")

# All PinYin in masterSentences.csv
msPinyins= []
for sentence in csv["Pronunciation2"]:
    for pronunciation in re.split(" |\.|\?", sentence):
        basePronunciation = unidecode.unidecode(pronunciation).lower()
        if basePronunciation != "" and basePronunciation not in msPinyins: 
            msPinyins.append(basePronunciation)


# All PinYin from pinYinTable.csv
pinYinList = pandas.read_csv("./pinYinTable.csv", encoding='utf-16-le')

# Initialize usage dict
masterInitialDict = {}
for initial in pinYinList.columns:
    masterInitialDict[initial] = 0
masterFinalDict = {}
for final in pinYinList.iloc[:,0]:
    masterFinalDict[final] = 0

# Get all finals and initials count used in sentences
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
finalsNeverUsedCount = len(finalsNeverUsed)
finalsKeyCount = len(masterFinalDict.keys())

initialsNeverUsed = [k for k, v in masterInitialDict.items() if v == 0]
initialsNeverUsedCount = len(initialsNeverUsed)
initialsKeyCount = len(masterInitialDict.keys()) 



# print results
print("DONE: Finals you used : %i /%i (%f)"%(finalsKeyCount - finalsNeverUsedCount, finalsKeyCount, 100-finalsNeverUsedCount*1.0/finalsKeyCount*100))
print("Let's use Finals below!")
print(finalsNeverUsed)

print("\nDONE: Initials you used : %i /%i (%f)"%(initialsKeyCount - initialsNeverUsedCount, initialsKeyCount, 100-initialsNeverUsedCount*1.0/initialsKeyCount*100))
print("Let's use initials below!")
print(initialsNeverUsed)

sentences = ""
for sentence in csv["Chinese"]:
    sentences += "%s\n\n\n\n\n\n"%sentence

pyperclip.copy(sentences)
print("\n\nCopied senttences to your clipboard. Visit https://ttsmp3.com/ and convert above to MP3!!")
webbrowser.open('https://ttsmp3.com/')  # Go to example.com


