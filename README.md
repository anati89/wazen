# WAZEN
**WAZEN** is an Arabic NLP text utility to find word variation pattern.
In this work three supervised machine learning algorithms were trained and validated on a 20k labeled words in order to detect the variation pattern of a given word which is a basic operation that is needed for NLP text in Arabic and about 96% accuracy was recorded.

And we are using the final models to develop an application that gives the root of the word based on the variation pattern.
```
Ex:
 -Input: مكالمة
 -Word variation pattern-مفاعلة :-الوزن الصرفي
 -Root-كلم :-الجذر
```

## Prerequisites:
 * Python 3.6
 * NLTK
 * scikit learn
 * dill

**Article talks about this project.** 


## How to use Wazen?
We already deployed the **three models** and the **feature extraction algorithm**:
- Naive Bayes: **naive.pkl**
- NN: **nn.pkl**
- SVM: **svm.pkl**

So all what you need is loading any model and feature extraction algorithm:



```python
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

#Sample:
nn_model, extract_features = load_model('nn.pkl')
feat = extract_features('مطوّر')
predict = nn_model.classify(feat)
print(predict)
مفعّل
```

## Root of word
The 1st application that take advantage for WAZEN is an rooting:
For that you need to run find_root.py
And enjoy with choosing the model and word:

```
الرجاء الاختيار من 1-3:
1: naiv bayes
2: NN bayes
3: SVM bayes
أي حرف آخر سيؤدي للخروج من البرنامج
2
ادخل الكملة من فضلك: مطوّر
مفعّل: الصيغة-
طور: الجذر-
```


## Contacts
Abdullah Al-Anati [LinkedIn](https://www.linkedin.com/in/abdullah-al-anati-56a13a53/)
Osama Sabri LinkedIn
