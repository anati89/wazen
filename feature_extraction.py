

class Word:
    """
    This class represents word as an object and has
    feature extraction method that is used to build matrix for each word
    based on most informative features by language experts
    """
    def __init__(self, word):
        self.word = word

    @staticmethod
    def extract_features(word):
        """
        Focus on word structure not frequency.
        Get features from word and store in dict
        """
        feat_3 = 1 if len(word) >= 4 and word[-1] == 'ن' else 0
        feat_4 = 1 if len(word) >= 5 and word[0:2] == 'ال' and word[0:4] != 'الأ'else 0
        feat_5 = 1 if len(word) >= 4 and word[1] == 'ا' else 0
        if feat_5:
            if word[3] == 'ا':
                feat_5 = 0
        feat_44 = 0
        if feat_4 and word[-1] == 'ى':
            feat_44 = 1
        feat_6 = 1 if len(word) >= 5 and word[-2:] == 'ات' else 0
        feat_7 = 1 if len(word) >= 5 and word[-2:] == 'ون' else 0
        feat_8 = 1 if len(word) >= 5 and word[-2:] == 'ين' else 0
        feat_9 = 1 if len(word) >= 5 and word[-2:] == 'ان' else 0
        feat_10 = 1 if len(word) >= 5 and word[-2:] == 'وا' else 0
        feat_11 = 1 if len(word) >= 4 and word[-2] == 'ي' else 0
        feat_12 = 1 if len(word) >= 4 and word[-2] == 'و' else 0
        feat_13 = 1 if len(word) >= 4 and word[-2] == 'ا' else 0
        feat_14 = 1 if len(word) >= 4 and word[-1] == 'ة' else 0
        feat_15 = 1 if len(word) >= 4 and word[-1] == 'ت' else 0
        feat_16 = 1 if len(word) >= 4 and word[0] == 'م' else 0
        feat_17 = 1 if len(word) >= 4 and word[0] == 'ي' else 0
        feat_18 = 1 if len(word) >= 4 and word[0] == 'أ' else 0
        feat_19 = 1 if len(word) >= 4 and word[0] == 'ن' else 0
        feat_47 = 1 if feat_19 and word[-2] == 'و' else 0
        feat_20 = 1 if len(word) >= 4 and word[0] == 'ت' else 0
        feat_21 = 1 if len(word) >= 4 and word[0] == 'ا' else 0
        feat_22 = 1 if 'ّ' in word else 0
        feat_23 = 1 if len(word) >= 4 and word[0] == 'ا' and word[-1] == 'ا' else 0
        feat_33 = 1 if len(word) >= 4 and word[0] == 'ا' and word[-1] == 'ي' else 0
        feat_27 = 0
        if feat_4:
            feat_27 = 1 if len(word) >= 4 and word[0] == 'ا' and word[-1] == 'ن' else 0
        feat_24 = 1 if len(word) >= 5 and word[0:3] == 'الأ' else 0
        feat_43 = 1 if feat_24 and word[-2] == 'و' else 0
        feat_35 = 0
        feat_46 = 0
        if not feat_24:
            feat_35 = 1 if len(word) >= 5 and word[3] == 'ا' else 0 # الجامح
            feat_46 = 1 if len(word) >= 5 and word[2] == 'ا' else 0 # ملاعب
        feat_25 = 1 if len(word) >= 3 and 'آ' in word else 0
        feat_26 = 1 if len(word) >= 4 and 'ي' in word else 0
        feat_28 = 1 if len(word) >= 5 and word[0:3] == 'الم' else 0
        feat_49 = 1 if len(word) >= 5 and word[0:4] == 'الما' else 0
        feat_29 = 1 if len(word) >= 4 and word[0] == 'م' else 0
        feat_30 = 1 if len(word) >= 5 and word[-2:] == 'نا' else 0
        feat_42 = 1 if len(word) >= 5 and word[-3:-1] == 'او' else 0
        feat_41 = 1 if len(word) >= 5 and word[-2:] == 'يا' else 0
        feat_31 = 1 if len(word) >= 4 and word[-1] == 'ى' else 0
        feat_32 = 1 if len(word) >= 5 and word[-2:] == 'تم' else 0
        feat_34 = 1 if len(word) == 4 and word[0] == 'ن' and word[-1] == 'ا' else 0
        feat_36 = 1 if len(word) >= 6 and 'ا' in word and 'ّا' in word else 0
        feat_48 = 1 if feat_28 and word[-3:-1] == 'او' else 0
        if feat_28:
            feat_29 = 1 if len(word) >= 4 and word[2] == 'م' else 0
        feat_37 = 0
        has_shaddeh_ = 0
        feat_38 = 0
        if feat_28 and word[-1] == 'ة':
            feat_37 = 1 if word[4] == 'ا' else 0
            feat_38 = 1 if word[4] == 'ّ' else 0
        feat_45 = 1 if feat_24 and word[-1] == 'ى' else 0
        feat_39 = 0
        if feat_28:
            feat_39 = 1 if word[-1] == 'ة' else 0
        feat_40 = 1 if len(word) >= 5 and word[0:4] == 'المت' else 0
        feat_50 = 1 if 'مم' in word else 0
        feat_dict = {
            # feat_1: Length of word
            'feat_1': len(word) + 1 if 'آ' in word else len(word),
            # feat_2: Length of word
            'feat_2': len(word) + 1 if 'آ' in word else len(word),
            # feat_3: ينتهي بالنون
            # مثال: منون , افعلن
            'feat_3': feat_3,
            #feat_4  يبدأ بال التعريف
            # الشاكر , الماجدات
            'feat_4': feat_4,  # Give more weighs for this feature by replication!
            #feat_5: يحتوي ألف
            # مثال: قال, صلاح
            'feat_5': feat_5,
            # feat_6: تبدأ (ألف تاء) ات
            # مثال: حامدات
            'feat_6': feat_6,
            # feat_7: ينتهي ب(واو نون) ون
            # مثال: شاكرون
            'feat_7': feat_7,
            # feat_8: ينتهي ب(ياء و نون) ان
            # مثال: شاكرين
            'feat_8': feat_8,
            # feat_9: ينتهي ب(ألف و نون) ان
            # مثال: شاكران
            'feat_9': feat_9,
            # feat_10: ينتهي ب(واو ألف) ان
            # مثال: شكروا
            'feat_10': feat_10,
            # feat_11: يحتوي حرف (ياء) قبل الآخر
            # مثال: قتيل
            'feat_11': feat_11,
            # feat_12: يحتوي حرف (واو) قبل الآخر
            # مثال: شكور
            'feat_12': feat_12,
            # feat_13: يحتوي حرف (الف) قبل الآخر
            # مثال: فلاح
            'feat_13': feat_13,
            # feat_14: ينتهي بتاء مربوطة(ة)
            # مثال: حديقة
            'feat_14': feat_14,
            # feat_15: ينتهي بتاء مفتوحة)
            # مثال: شكرت
            'feat_15': feat_15,
            # feat_16: يبدأ ب(ميم) م
            # مثال: فعلتم, نلتم
            'feat_16': feat_16,
            # feat_17: يبدأ ب(ياء) ي
            # مثال: يحصل
            'feat_17': feat_17,
            # feat_18: يبدأ ب(همزة) ء
            # مثال: أكل
            'feat_18': feat_18,
            # feat_19: يبدأ ب(نون) ن
            # مثال: نلعب
            'feat_19': feat_19,
            # feat_20: يبدأ ب(تاء) ت
            # مثال: تلعب
            'feat_20': feat_20,
            # feat_21: يبدأ ب(الف) ا
            # مثال: العب
            'feat_21': feat_21,
            # feat_22: تحتوي شدة
            # مثال: صدّيق
            'feat_22': feat_22,
            # feat_23: تبدأ الف تنتهي الف
            # مثال: احصلا
            'feat_23': feat_23,
            # feat_24: تبدأ (ألف لام همزة) الأ
            # مثال: الأكثر
            'feat_24': feat_24,
            # feat_25: يحتوي مد
            # مثال: مآل
            'feat_25': feat_25,
            # feat_26: يحتوي ياء أي مكان
            # مثال: كثير
            'feat_26': feat_26,
            # feat_27: يبدأ(الف ينتهي نون) ان
            # صادقان
            'feat_27': feat_27,
            # feat_28: يبدأ(الف لام ميم) الم
            # المستحيل
            'feat_28': feat_28,
            # feat_29: يحتوي (ميم) ميم
            # مثال: المستحيل
            'feat_29': feat_29,
            # feat_30: ينتهي ي (نون الف) نا
            # مثال: ركضنا
            'feat_30': feat_30,
            # feat_31: ينتهي ب (ألف مقصورة) ى
            # مثال: كبرى
            'feat_31': feat_31,
            # feat_32: ينتهي ب (ألف تاء ميم) تم
            # مثال: كبرى
            'feat_32': feat_32,
            # feat_33: يبدأ الف ينتهي ياء
            # مثال: اركضي
            'feat_33': feat_33,
            # feat_34: يبدأ نون ينتهي الف
            # مثال: نقلنا
            'feat_34': feat_34,
            # feat_35: يحتوي الف كحرف ثالث أو رابع
            # مثال: ملامح, الجامح
            'feat_35': feat_35,
            # feat_36: يحتوي شدة ثم الف
            # مثال: حفّار
            'feat_36': feat_36,
            # feat_37: يبدأ ب (ألف لام ميم) المـ
            # مثال: المعالم
            'feat_37': feat_37,
            # feat_38: يبدأ ب (ألف لام ميم) ينتهي بتاء مربوطه و حرفه الخامس شدة
            # مثال: الميسّرة
            'feat_38': feat_38,
            # feat_39: يبدأ ب (ألف لام ميم) ينتهي بتاء مربوطه
            # مثال: الميسرة
            'feat_39': feat_39,
            # feat_40: يبدأ ب (ألف لام ميم تاء)
            # مثال: المتعلّم
            'feat_40': feat_40,
            # feat_41: ينتهي ب(ياء الف) يا
            # مثال: لقيا
            'feat_41': feat_41,
            # feat_42: يحتوي  واو الف
            # مثال: المقاول
            'feat_42': feat_42,
            # feat_43: يبدأ  الف لام و ينتهي بواو
            # مثال: الأقاول
            'feat_43': feat_43,
            # feat_44: يبدأ ب(الف و لام) التعريف وينتهي بألف مقصورة
            # مثال: الكبرى
            'feat_44': feat_44,
            # feat_45: يبدأ ب(الف و لام و همزة) -الأ- وينتهي بألف مقصورة
            # مثال: الأسمى
            'feat_45': feat_45,
            # feat_46: يحتوي ألف ثالث أو رابع
            # مثال: ملاعب, الجامح
            'feat_46': feat_46,
            # feat_47: يبدأ بنون و يحتوي واو قبل الأخير
            # مثال: نسور
            'feat_47': feat_47,
            # feat_48: يبدأ ب(ألف لاوم ميم) و يحتوي (واو الف) قبل الأخير
            # مثال: المقاول
            'feat_48': feat_48,
            # feat_49: يبدأ ب(ألف لاوم ميم الف) -الما-
            # مثال: المارق
            'feat_49': feat_49,
            # feat_50: يحتوي (ميم ميم)
            # مثال: الممسحة
            'feat_50': feat_50,
        }
        return feat_dict


def get_lines(file_name):
    """
    Read file called data.txt and return generator of lists
    list of index 0: verb
    list of index 1: wazen
    :return:
    """
    verbs_wazens = (line.strip().split() for line in open(file_name, encoding='utf-8')
                    if line.strip())
    return verbs_wazens


def get_data_target(file_name='data.txt'):
    """
    Reads word from file and extracts features
    Then append data and feature
    :return: Data, Target
    """
    verb_wazen = get_lines(file_name)
    Data = []
    Target = []
    for sub_list in verb_wazen:
        wazen, verb = sub_list[1], sub_list[0]
        word = Word(verb)
        features = word.extract_features(word.word)
        Data.append(list(features.values()))
        Target.append(wazen)
    return Data, Target