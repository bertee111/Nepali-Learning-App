import random

verbs = {
    '1': ['To be', 'हुनु', 'hunu'],
    '2': ['To cry', 'रुनु', 'runu'],
    '3': ['To eat', 'खानु', 'khānu'],
    '4': ['To go', 'जानु', 'jānu'],
    '5': ['To touch', 'छुनु', 'chunu'],
    '6': ['To come', 'आउनु', 'āunu'],
    '7': ['To cook', 'पकाउनु', 'pakāunu'],
    '8': ['To accept', 'स्वीकार गर्नुहोस्', 'Svīkāra garnuhōs'],
    '9': ['To add', 'थप्नुहोस्', 'thapnuhōs'],
    '10': ['To allow', 'अनुमति दिनुहोस्', 'anumati dinuhōs'],
    '11': ['To answer', 'जवाफ', 'javāpha'],
    '12': ['To arrive', 'आइपुग्छ', 'ā’ipugcha'],
    '13': ['To ask', 'सोध्नु', 'sōdhnu'],
    '14': ['To become', 'बन्नु', 'bannu'],
    '15': ['To believe', 'विश्वास', 'viśvāsa'],    
    '16': ['To break', 'ब्रेक', 'brēka'],
    '17': ['To bring', 'ल्याउनुहोस्', 'lyā’unuhōs'],
    '18': ['To call', 'कल', 'kala'],
    '19': ['To change', 'परिवर्तन', 'parivartana'],
    '20': ['To choose', 'चान्नुहोस्', 'chānnuhōs'],
    '21': ['To clean', 'सफा', 'saphā'],
    '22': ['To close', 'बन्द', 'banda'],
    '23': ['To come back', 'फिर्ता आउनुहोस्', 'phirtā ā’unuhōs'],
    '24': ['To continue', 'जारी राख्नुहोस्', 'jārī rākhnuhōs'],
    '25': ['To count', 'गणना', 'gaṇanā'],
    '26': ['To decide', 'निर्णय', 'nirṇaya'],
    '27': ['To do', 'गर्नु', 'garnu'],
    '28': ['To drive', 'ड्राइभ', 'ḍrā’ibha'],
    '29': ['To enter', 'प्रविष्ट गर्नुहोस्', 'praviṣṭa garnuhōs'],
    '30': ['To exist', 'अवस्थित छ', 'avasthita cha'],
    '31': ['To explain', 'व्याख्या गर्नुहोस्', 'vyākhyā garnuhōs'],
    '32': ['To fall', 'पटन', 'patana'],
    '33': ['To fall asleep', 'सुत्नु', 'sutnu'],
    '34': ['To find', 'फेला पार्नुहोस्', 'phēlā pārnuhōs'],
    '35': ['To finish', 'समाप्त', 'samāpta'],
    '36': ['To fly', 'उड्नु', 'uḍnu'],
    '37': ['To follow', 'पछ्याउनु', 'pachyā’una'],
    '38': ['To forget', 'बिर्सनु', 'birsanu'],
    '39': ['To get off', 'बाहिर जानुहोस्', 'bāhira jānuhōs'],
    '40': ['To get out', 'बाहिर जाउ', 'bāhira jā’ū'],
    '41': ['To give', 'दिनु', 'dinu'],
    '42': ['To have', 'छ', 'cha'],
    '43': ['To hear', 'सुन्नुहोस्', 'sunnuhōs'],
    '44': ['To help', 'मद्दत', 'maddata'],
    '45': ['To hold', 'होल्ड गर्नुहोस्', 'hōlḍa garnuhōs'],
    '46': ['To keep', 'राख्न', 'rākhna'],
    '47': ['To know', 'जान्नुहुन्छ', 'jānnuhuncha'],
    '48': ['To laugh', 'हाँस्न', 'hām̐sna'],
    '49': ['To learn', 'सिक्नुहोस्', 'siknuhōs'],
    '50': ['To leave', 'छोड', 'chōḍa'],
    '51': ['To listen', 'सुन्नुहोस्', 'sunnuhōs'],
    '52': ['To live', 'लाइब्ह', 'lā’ibha'],
    '53': ['To look like', 'जस्तो देखिन्छ', 'jastō dēkhincha'],
    '54': ['To look', 'हेर', 'hēra'],
    '55': ['To lose', 'हाराउनु', 'harā’unu'],
    '56': ['To love', 'माया', 'māyā'],
    '57': ['To make', 'बनाउनु', 'banā’una'],
    '58': ['To meet', 'भेट्न', 'bhēṭna'],
    '59': ['To need', 'आवश्यकता', 'āvaśyakatā'],
    '60': ['To open', 'खोल्नुहोस्', 'khōlnuhōs'],
    '61': ['To pay', 'भुक्तान', 'bhuktāna'],
    '62': ['To play', 'खेल्नु', 'khēlnu'],
    '63': ['To prepare', 'तयारी', 'tayārī'],
    '64': ['To prevent', 'रोकथामा', 'rōkathāma'],
    '65': ['To put', 'राख्नु', 'rākhnu'],
    '66': ['To read', 'पढ्नुहोस्', 'paḍhnuhōs'],
    '67': ['To recall', 'सम्झना', 'samjhanā'],
    '68': ['To receive', 'प्राप्त गर्नुहोस्', 'prāpta garnuhōs'],
    '69': ['To recognize', 'पहिचान', 'pahicāna'],
    '70': ['To refuse', 'अस्वीकार', 'asvīkāra'],
    '71': ['To remember', 'सम्झनु', 'samjhanu'],
    '72': ['To repeat', 'दोहोर्याउनुहोस्', 'dōhōryā’unuhōs'],
    '73': ['To rest', 'विश्राम', 'viśrāma'],
    '74': ['To return', 'फर्किनु', 'pharkinu'],
    '75': ['To run', 'दौडनु', 'dauḍanu'],
    '76': ['To say', 'भन्नुहोस्', 'bhannuhōs'],
    '77': ['To search', 'खोज', 'khōja'],
    '78': ['To see', 'हेर्नुहोस्', 'hernuhōs'],
    '79': ['To sell', 'बेच्नुहोस्', 'bēcnuhōs'],
    '80': ['To send', 'पठाउनुहोस्', 'paṭhā’unuhōs'],
    '81': ['To shoot', 'गोली मार', 'gōlī māra'],
    '82': ['To show', 'देखाउनु', 'dēkhā’unu'],
    '83': ['To sing', 'गाउनुहोस्', 'gā’unuhōs'],
    '84': ['To sit down', 'बस', 'basa'],
    '85': ['To sleep', 'सुत्नु', 'sutnu'],
    '86': ['To start', 'सुरु', 'suru'],
    '87': ['To stay', 'रहनु', 'rahanu'],
    '88': ['To stop', 'रोक', 'rōka'],
    '89': ['To succeed', 'सफल', 'saphala'],
    '90': ['To switch off', 'बन्द गर्नुहोस्', 'banda garnuhōs'],
    '91': ['To take', 'लिनुहोस्', 'linuhōs'],
    '92': ['To talk', 'कुरा', 'kurā'],
    '93': ['To taste', 'स्वाद', 'svāda'],
    '94': ['To think', 'सोच्नुहोस्', 'sōcnuhōs'],
    '95': ['To throw', 'फाल्नु', 'phālnu'],
    '96': ['To touch', 'स्पर्श', 'sparśa'],
    '97': ['To try', 'प्रयास गर्नुहोस्', 'prayāsa garnuhōs'],
    '98': ['To turn', 'घुमाउनुहोस्', 'ghumā’unuhōs'],
    '99': ['To turn on', 'खोल्नुहोस्', 'khōlnuhōs'],
    '100': ['To understand', 'बुझ्नुहोस्', 'bujhnuhōs'],
    '101': ['To use', 'प्रयोग गर्नुहोस्', 'prayōga garnuhōs'],
    '102': ['To wait', 'पर्खनुहोस्', 'parkhanuhōs'],
    '103': ['To wake up', 'उठ्नुहोस्', 'uṭhnuhōs'],
    '104': ['To walk', 'हिड्नु', 'hiḍnu'],
    '105': ['To want', 'चाहन्छ', 'cāhancha'],
    '106': ['To wash up', 'धुनुहोस्', 'dhunuhōs'],
    '107': ['To wear', 'लगाउनु', 'lagāunu'],
    '108': ['To win', 'जित', 'jīta'],
    '109': ['To work', 'काम', 'kāma'],
    '110': ['To write', 'लेख्नुहोस्', 'lēkhnuhōs'],
    '111': ['To drink', 'पिउनु', 'piunu'],
    '112': ['To slip', 'चिप्लनु', 'ciplanu'],
    '113': ['To stand', 'उभिनु', 'ubhinu'],
}

consonants = {
    1: ['क', 'ka'],
    2: ['ख', 'kʰa'],
    3: ['ग', 'ga'],
    4: ['घ', 'gʰa'],
    5: ['ङ', 'ŋa'],
    6: ['च', 'cha'],
    7: ['छ', 'chʰa'],
    8: ['ज', 'ja'],
    9: ['झ', 'jʰa'],
    10: ['ञ', 'ɲa'],
    11: ['ट', 'ʈa'],
    12: ['ठ', 'ʈʰa'],
    13: ['ड', 'ɖa'],
    14: ['ढ', 'ɖʰa'],
    15: ['ण', 'ɳa'],
    16: ['त', 't̪a'],
    17: ['थ', 't̪ʰa'],
    18: ['द', 'd̪a'],
    19: ['ध', 'd̪ʰa'],
    20: ['न', 'na'],
    21: ['प', 'pa'],
    22: ['फ', 'pʰa'],
    23: ['ब', 'ba'],
    24: ['भ', 'bʰa'],
    25: ['म', 'ma'],
    26: ['य', 'ya'],
    27: ['र', 'ra'],
    28: ['ल', 'la'],
    29: ['व', 'wa'],
    30: ['स', 'sa'],
    31: ['श', 'sha'],
    32: ['ष', 'ṣa'],
    33: ['ह', 'ha'],
    34: ['क्ष', 'chʰya'],
    35: ['त्र', 't̪ra'],
    36: ['ज्ञ', 'gya'],
}

vowels = {
    1: ['अ', 'a'],
    2: ['आ', 'ā'],
    3: ['इ', 'i'],
    4: ['ई', 'ī'],
    5: ['उ', 'u'],
    6: ['ऊ', 'ū'],
    7: ['ए', 'e'],
    8: ['ऐ', 'ai'],
    9: ['ओ', 'o'],
    10: ['औ', 'au'],
}

dependent_vowels = {
    1: ['ा', 'ā'],
    2: ['ि', 'i'],
    3: ['ी', 'ī'],
    4: ['ु', 'u'],
    5: ['ू', 'ū'],
    6: ['े', 'e'],
    7: ['ै', 'ai'],
    8: ['ो', 'o'],
    9: ['ौ', 'au'],
}

anusvara_dict = {
    1: ['ं', 'ṁ'],  # Anusvara
}

visarga_dict = {
    1: ['ः', ':'],  # Visarga
}
numeral_dict = {
    0: ['०', 'शुन्य/सुन्ना', 'śūnya', 0],
    1: ['१', 'एक', 'ek', 1],
    2: ['२', 'दुई', 'duī', 2],
    3: ['३', 'तीन', 'tīn', 3],
    4: ['४', 'चार', 'cār', 4],
    5: ['५', 'पाँच', 'pāṃc', 5],
    6: ['६', 'छ', 'cha', 6],
    7: ['७', 'सात', 'sāt', 7],
    8: ['८', 'आठ', 'āṭh', 8],
    9: ['९', 'नौ', 'nau', 9],
    10: ['१०', 'दस', 'daś', 10],
    11: ['११', 'एघार', 'eghāra', 11],
    12: ['१२', 'बाह्र', 'bāhra', 12],
    13: ['१३', 'तेह्र', 'tehra', 13],
    14: ['१४', 'चौध', 'chaudha', 14],
    15: ['१५', 'पन्ध्र', 'pandhra', 15],
    16: ['१६', 'सोह्र', 'sohra', 16],
    17: ['१७', 'सत्र', 'satra', 17],
    18: ['१८', 'अठार', 'atthahra', 18],
    19: ['१९', 'उन्नाइस', 'unnais', 19],
    20: ['२०', 'बीस', 'bīs', 20],
    21: ['२१', 'एक्काइस', 'ekkāis', 21],
    22: ['२२', 'बाइस', 'bāis', 22],
    23: ['२३', 'तेइस', 'teis', 23],
    24: ['२४', 'चौबीस', 'chaubīs', 24],
    25: ['२५', 'पच्चीस', 'pacchīs', 25],
    26: ['२६', 'छब्बीस', 'chhabbīs', 26],
    27: ['२७', 'सत्ताइस', 'sattāis', 27],
    28: ['२८', 'अठ्ठाइस', 'aṭṭhāis', 28],
    29: ['२९', 'उनन्तीस', 'unantīs', 29],
    30: ['३०', 'तीस', 'tīs', 30],
    31: ['३१', 'एकतीस', 'ekatīs', 31],
    32: ['३२', 'बत्तीस', 'battīs', 32],
    33: ['३३', 'तेतीस', 'tetīs', 33],
    34: ['३४', 'चौतीस', 'chaūtīs', 34],
    35: ['३५', 'पैंतीस', 'paiṁtīs', 35],
    36: ['३६', 'छत्तीस', 'chhattīs', 36],
    37: ['३७', 'सैंतीस', 'saiṁtīs', 37],
    38: ['३८', 'अठतीस', 'aṭhatīs', 38],
    39: ['३९', 'उनन्चालीस', 'unancālīs', 39],
    40: ['४०', 'चालीस', 'cālīs', 40],
    41: ['४१', 'एकचालीस', 'ekacālīs', 41],
    42: ['४२', 'बयालीस', 'bayālīs', 42],
    43: ['४३', 'त्रिचालीस', 'tricālīs', 43],
    44: ['४४', 'चवालीस', 'cavālīs', 44],
    45: ['४५', 'पैँतालीस', 'paiṁtālīs', 45],
    46: ['४६', 'छयालीस', 'chayālīs', 46],
    47: ['४७', 'सत्चालीस', 'saccālīs', 47],
    48: ['४८', 'अठचालीस', 'aṭhcālīs', 48],
    49: ['४९', 'उनन्चास', 'unancās', 49],
    50: ['५०', 'पचास', 'pacās', 50],
    51: ['५१', 'एकाउन्न', 'ekāunn', 51],
    52: ['५२', 'बाउन्न', 'bāunn', 52],
    53: ['५३', 'त्रिपन्न', 'tripann', 53],
    54: ['५४', 'चवन्न', 'cavann', 54],
    55: ['५५', 'पचपन्न', 'pacapann', 55],
    56: ['५६', 'छपन्न', 'chapann', 56],
    57: ['५७', 'सत्पन्न', 'satpann', 57],
    58: ['५८', 'अठपन्न', 'aṭhpann', 58],
    59: ['५९', 'उनन्साठी', 'unnasāṭhī', 59],
    60: ['६०', 'साठी', 'sāṭhī', 60],
    61: ['६१', 'एकसठी', 'ekasāṭhī', 61],
    62: ['६२', 'बैसठी', 'baisāṭhī', 62],
    63: ['६३', 'त्रिसठी', 'trisāṭhī', 63],
    64: ['६४', 'चौंसठी', 'chaunsāṭhī', 64],
    65: ['६५', 'पैंसठी', 'paiṁsāṭhī', 65],
    66: ['६६', 'छैंसठी', 'chhaiṁsāṭhī', 66],
    67: ['६७', 'सत्सठी', 'satsāṭhī', 67],
    68: ['६८', 'अठसठी', 'aṭhsāṭhī', 68],
    69: ['६९', 'उनन्सत्ताई', 'unnansattāī', 69],
    70: ['७०', 'सत्ताई', 'sattāī', 70],
    71: ['७१', 'एकहत्ताई', 'ekahattāī', 71],
    72: ['७२', 'बहत्ताई', 'bahattāī', 72],
    73: ['७३', 'त्रिहत्ताई', 'trihattāī', 73],
    74: ['७४', 'चौहत्ताई', 'cauhattāī', 74],
    75: ['७५', 'पचहत्ताई', 'pachhattāī', 75],
    76: ['७६', 'छयहत्ताई', 'chhayahattāī', 76],
    77: ['७७', 'सत्तहत्ताई', 'sattahattāī', 77],
    78: ['७८', 'अठहत्ताई', 'aṭhhattāī', 78],
    79: ['७९', 'उनन्सत्याई', 'unnansatyāī', 79],
    80: ['८०', 'अस्सी', 'assī', 80],
    81: ['८१', 'एकास्सी', 'ekāssī', 81],
    82: ['८२', 'बयास्सी', 'byāssī', 82],
    83: ['८३', 'त्रियास्सी', 'triyāssī', 83],
    84: ['८४', 'चौरास्सी', 'caurāssī', 84],
    85: ['८५', 'पचास्सी', 'pacāssī', 85],
    86: ['८६', 'छयास्सी', 'chhayāssī', 86],
    87: ['८७', 'सतास्सी', 'satāssī', 87],
    88: ['८८', 'अठास्सी', 'aṭhāssī', 88],
    89: ['८९', 'उनन्नब्बे', 'unnannabbe', 89],
    90: ['९०', 'नब्बे', 'nabbe', 90],
    91: ['९१', 'एकानब्बे', 'ekānabbe', 91],
    92: ['९२', 'बानब्बे', 'bānabbe', 92],
    93: ['९३', 'त्रियानब्बे', 'triyānabbe', 93],
    94: ['९४', 'चौरानब्बे', 'caurānabbe', 94],
    95: ['९५', 'पचानब्बे', 'pacānabbe', 95],
    96: ['९६', 'छयानब्बे', 'chhayānabbe', 96],
    97: ['९७', 'सन्तानब्बे', 'santānabbe', 97],
    98: ['९८', 'अठानब्बे', 'aṭhānabbe', 98],
    99: ['९९', 'उनन्सय', 'unnansaya', 99],
    100: ['१००', 'एक सय', 'ek saya', 100],
}

def verbs_question():
    random_key, random_value = random.choice(list(verbs.items()))
    direction = random.choice(['english_to_nepali', 'nepali_to_english'])

    if direction == 'english_to_nepali':
        question = random_value[0]
        correct_answer = random_value[2]
    else:
        question = random_value[2]
        correct_answer = random_value[0]
    formatted_answer = [s.replace('ā','a')
                            .replace('ī','i')
                            .replace('ō','o')
                            .replace('ē','e')
                            .replace('m̐','m')
                            .replace('ḍ','d')
                            .replace('ṭ','t')
                            .replace('ś','s')
                            .replace('ṣ','s')
                            .replace('’','`')
                            .replace('ṇ','n')
                            for s in correct_answer] 
    user_answer = input('What is translation of ' + question + '? ')
    
    if user_answer.lower() == ''.join(formatted_answer).lower():
        print('Correct answer!, it was indeed ', correct_answer)
    else:       
        print('Wrong answer. The correct answer is:', correct_answer)


def consonants_question():
    print('consonant')

def vowel_question():
    print('vowel')

def dependent_vowel_question():
    print('dependent')


def game(consonant, vowel, dependent_vowel, verbs):
    
    categories = {
        '1': ('Consonants', consonants_question, consonant),
        '2': ('Vowels',vowel_question, vowel),
        '3': ('Dependent Vowels',dependent_vowel_question, dependent_vowel),
        '4': ('Verbs',verbs_question, verbs),
    }
    categories_selection = input('''What would you like to practice today?\n
        1)Consonants?\n
        2)Vowels\n
        3)Dependent Vowels\n
        4)Verbs\n
        (You can play multiple categories at the same time!\n''')
    selected_categories = [categories[i]for i in categories_selection if i in categories]
    print('Selected categories:')
    for category_info in selected_categories:
        # category_name, _, _ = category_info
        # print('-',category_name)
        print('-', category_info[0])
    while True:
        random_category = random.choice(selected_categories)
        print('The question is in the category:', random_category[0])
        # _, random_question_function, _ = random_category
        # random_question_function()
        random_question_function = random_category[1]
        random_question_function()
        next = input('press enter to go next')
        if next == '':
            continue
        else:
            break


    
game(consonants, vowels, dependent_vowels, verbs)            




    


    
# game(consonant_dict, game_consonant_dict, vowel_dict, game_vowel_dict, dependent_vowel_dict, game_dependent_vowel_dict)



# while True:
#     try:
#         verbs[random_key] = game_verbs.pop(random_key)
#     except: KeyError

#     random_key, random_value = random.choice(list(verbs.items()))
#     game_verbs[random_key] = verbs.pop(random_key)
#     random_key_two, random_value_two = random.choice(list(verbs.items()))
#     randomquestion = random.choice([0,2])
#     print(random_key, random_value[randomquestion])
#     answer = input('What is the translation?\n')
#     if randomquestion == 2:
#         if answer == str(random_value[0]).lower():
#             print('Correct answer!')
#         elif answer != str(random_value[0]).lower():
#             print('Wrong answer, heres a tip,\nits either', random_value_two[0],'or', random_value[0])
#             answer_two = input('which is it?')
#             if answer_two == str(random_value[0]).lower() :
#                 print('correct answer!\nLets try again\n')
#             else:
#                 print('Wrong answer\nThe answer was',random_value[0],'lets try again!\n')          
#     if randomquestion == 0:
#         new_value = [s.replace('ā','a').replace('ī','i').replace('ō','o').replace('ē','e').replace('m̐','m').replace('ḍ','d').replace('ṭ','t').replace('ś','s').replace('’','`') for s in random_value]
#         if answer == (new_value[2]):
#             print('Correct answer!\nThe answer was',random_value[2],'\n')
#         elif answer != str(random_value[2]).lower():
#             print('Wrong answer, heres a tip,\nits either', random_value_two[2],'or', random_value[2])
#             answer_two = input('which is it?\n')
#             if answer_two == new_value[2]:
#                 print('correct answer!\nLets try again\n')
#             else:
#                 print('Wrong answer!\nThe answer was',random_value[2],'\n')
