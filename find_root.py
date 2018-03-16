"""*************##########################****************
    This is an application for find root using wazen models
    Author:Abdullah Al-Anati
    email: anati_just@yahoo.com
*************##########################****************
"""
import sys
import dill as pickle

def load_model(pkl_file):
    """
    Load pickle model and feature extraction function
    :param pkl_file:
    :return: loaded_model, extract_features
    """
    fp = open(pkl_file, 'rb')
    loaded_model = pickle.load(fp)
    extract_features = pickle.load(fp)
    fp.close()
    return loaded_model, extract_features


def find_root(word):
    """
    This function is used to find the index of basic letters
    in variation pattern and get matched in real word
    :param word:
    :return: first_letter, second_letter, third_letter
    """
    first_letter = word.find('ف')
    second_letter = word.find('ع', )
    third_letter = word.rfind('ل')
    if first_letter == -1 or second_letter == -1 or third_letter == -1:
        sys.exit('عدد الحروف لا يكفي لاستخراج الجذر!')
    return first_letter, second_letter, third_letter


def main():
    """Main func"""
    print(__doc__)
    nb_model, extract_features = load_model('naive.pkl')
    nn_model, extract_features = load_model('nn.pkl')
    svm_model, extract_features = load_model('svm.pkl')
    options = {
        1: 'naiv',
        2: 'nn',
        3: 'svm'
    }
    msg = 'الرجاء الاختيار من 1-3:' \
    '\n1: naiv bayes' \
    '\n2: NN bayes' \
    '\n3: SVM bayes' \
    '\nأي حرف آخر سيؤدي للخروج من البرنامج\n' \

    while True:
        try:
            user_input = int(input(msg))
        except:
            print('الخروج من البرنامج')
            sys.exit()
        if user_input not in list(options):
            print('الخروج من البرنامج')
            break
        word = input('ادخل الكملة من فضلك: ')
        if len(word.split()) > 1:
            print('يجب ادخال كلمة واحدة!')
            print('الخروج من البرنامج')
            sys.exit()
        feat = extract_features(word)
        if user_input == 1:
            predict = nb_model.classify(feat)
        elif user_input == 2:
            predict = nn_model.predict([list(feat.values())])
            predict = predict[0]
        elif user_input == 3:
            predict = svm_model.predict([list(feat.values())])
            predict = predict[0]
        print(f'{predict}: الصيغة-')
        first_letter, second_letter, third_letter = find_root(predict)
        print(f'{word[first_letter]}{word[second_letter]}{word[third_letter]}: الجذر-')


if __name__ == "__main__":
    main()