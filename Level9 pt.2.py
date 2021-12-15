slangDict = {'BRB' : 'be right Back', 'DP' : 'Dsplay Picture', 'LMAO' : 'laugh my ass off'
             , 'LOL' : 'Laughing out load' , 'OK' : 'Olla kalla or Oll Korrect' , 'PFA' : '''Please find attachment,
             Predictive FAilure analysis''' , 'ROFL' : 'Rolling on floor laughing' , 'TBH' : 'to be honest' , 
             'TTYL' : 'Talk to you later' , "Eta" : ' Estimated Time to Arrival', "FYI" : 'For your information'}

def SlangTranslator():
    print('Enter the slang you want translation for. ')
    word = input().upper()
    print(f'The meaning is {slangDict.get(word, "is not in this dict. yet")}')
        
        
SlangTranslator()