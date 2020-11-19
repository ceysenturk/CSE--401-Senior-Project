import speech_recognition as sr
from gtts import gTTS
import os
import Tokenizer
import questionfile
import answerfile


r = sr.Recognizer()
result = ""
sentence = ""
keyList = []
keyListBeta = []
tempList = []

questionList = questionfile.questionfunction()
answerList = answerfile.answerfunction()


def takeQuestion():

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            print("Sizi dinliyorum...")
            data = r.record(source, duration=10)

            print("Sesiniz Metine Dönüştürülüyor…")
            global sentence
            sentence = r.recognize_google(data, language='tr')
        print("\nSorunuz: " + sentence)


def analyzeQuestion():
    # analyze the sentence
    wordList = Tokenizer.analyze(sentence)
    # Show word list
    print("\nTokenized Sentence")
    print(wordList)

    for word in wordList:
        if len(keyList) < 3:
            for item in questionList:
                if (word in item[0]) or (item[0] in word):
                    keyList.append(item[0])
                    break
                elif (word in item[1]) or (item[1] in word):
                    keyList.append(item[1])
                    break
                elif (word in item[2]) or (item[2] in word):
                    keyList.append(item[2])
                    break
        else:
            break

    print("\nKey Words: ")
    print(keyList)

    keyListBeta.append(keyList)

def analyzeAnswer():
    for i in range(len(answerList)):
        sentence = answerList[i]
        wordList = Tokenizer.analyze(sentence)
        for word in (wordList):
            if len(tempList) < 3:
                for item in keyListBeta:
                    if (word in item[0]) or (item[0] in word):
                        tempList.append(item[0])
                        break
                    elif (word in item[1]) or (item[1] in word):
                        tempList.append(item[1])
                        break
                    elif (word in item[2]) or (item[2] in word):
                        tempList.append(item[2])
                        break
            else:
                break

        if sorted(keyList) == sorted(tempList):
            print("\nCevap:")
            print(sentence)
            tts = gTTS(text=sentence, lang='tr')
            tts.save("answer.mp3")
            os.system("answer.mp3")
            break
        else:
            tempList.clear()


def main():

    takeQuestion()
    analyzeQuestion()
    analyzeAnswer()

if __name__ == '__main__':
    main()