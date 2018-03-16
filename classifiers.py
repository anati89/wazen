import dill as pickle
import nltk
import nltk.classify
from sklearn.svm import LinearSVC
import numpy as np
import statistics
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

#Local modules
import feature_extraction

def split_data(data, target):
    """
    Split all data into:
    training: 70%
    testing: 30%
    :param Data:
    :param Target:
    :return:
    """
    train_data, test_data, train_target, test_target = train_test_split(
        data, target, test_size=0.3, random_state=1)
    print(f'Total number of data: {len(data)}')
    print('Total data is split into: training(70%) & testing(30%)')
    print(f'  --> Training data words: {len(train_data)}')
    print(f'  --> Testing Data words: {len(test_data)}')
    return train_data, train_target, test_data, test_target


def apply_kfold(clf, data, target):
    kf = KFold(n_splits=10)
    sum = 0
    accuracy_list = []
    for train_indices, test_indices in kf.split(data):
        train_data = np.array(data)[train_indices]
        test_data = np.array(data)[test_indices]
        train_target = np.array(target)[train_indices]
        test_target = np.array(target)[test_indices]
        clf.fit(train_data, train_target)
        skill = clf.score(test_data, test_target)
        accuracy_list.append(skill)
        sum += skill
    average = sum / 10
    std = statistics.stdev(accuracy_list)
    return average, std


def nn_classifier(train_data, train_target, test_data, test_target):
    """
    Train and test using MLP classier
    :param train_data:
    :param train_target:
    :param test_data:
    :param test_target:
    :return:
    """
    MLP_clf = MLPClassifier(solver='adam', alpha=1e-3,
                            activation='identity',
                            hidden_layer_sizes=(90, 110), random_state=1)
    mlp_avg, mlp_sd = apply_kfold(MLP_clf, train_data, train_target)
    print(f'NN KFold Accuracy: {mlp_avg} std: {mlp_sd}')
    model = MLP_clf.fit(train_data, train_target)
    acc = model.score(test_data, test_target)
    print(f'NN final model accuracy: {acc}')
    ##dump model
    dump_model(model, 'nn.pkl')


def svm_classifier(train_data, train_target, test_data, test_target):
    """
    Train and test using SVM classier
    :param train_data:
    :param train_target:
    :param test_data:
    :param test_target:
    :return:
    """
    svm_clf = LinearSVC()
    svm_avg, svm_sd = apply_kfold(svm_clf, train_data, train_target)
    print(f'SVM KFold Accuracy: {svm_avg} std: {svm_sd}')
    model = svm_clf.fit(train_data, train_target)
    acc = model.score(test_data, test_target)
    print(f'SVM final model accuracy: {acc}')
    ##dump model
    dump_model(model, 'svm.pkl')


def format_nltk_inputs(input, target):
    """
    Prepare NLTK inputs as tuple of dict and target
    :return:
    """
    input_nltk = []
    for input_feat, tar in zip(input, target):
        list_dict = {}
        for index, feat_val in enumerate(input_feat):
            index = index + 1
            k = f'feat_{index}'
            list_dict[k] = feat_val
        input_nltk.append((list_dict, tar))
    return input_nltk


def nb_classifier(train_data, train_target, test_data, test_target):
    """
    Train and test using Naive Bayes classier
    :param train_data:
    :param train_target:
    :param test_data:
    :param test_target:
    :return:
    """
    train_nltk_input = format_nltk_inputs(train_data, train_target)
    kf = KFold(n_splits=10)
    sum = 0
    acc_list = []
    for train_indices, test_indices in kf.split(train_nltk_input):
        train_data_ = np.array(train_nltk_input)[train_indices]
        test_data_ = np.array(train_nltk_input)[test_indices]
        clf = nltk.NaiveBayesClassifier.train(train_data_)
        acc = nltk.classify.accuracy(clf, test_data_)
        acc_list.append(acc)
        sum += acc
    average = sum / 10
    std = statistics.stdev(acc_list)
    print(f'NLTK Accuracy on train data using K-fold: {average} std: {std}')
    test_nltk_input = format_nltk_inputs(test_data, test_target)
    model = nltk.NaiveBayesClassifier.train(train_nltk_input)
    acc = nltk.classify.accuracy(model, test_nltk_input)
    print(f'NLTK accuracy on testing data {acc}')
    ##dump model
    dump_model(model, 'naive.pkl')


def dump_model(model, pkl_name):
    """Save model as pickle file"""
    fp = open(pkl_name, 'wb')
    pickle.dump(model, fp)
    pickle.dump(feature_extraction.Word.extract_features, fp)
    fp.close()


def main():
    """Main func"""
    Data, Target = feature_extraction.get_data_target('data.txt')
    train_data, train_target,\
    test_data, test_target = split_data(Data, Target)
    nn_classifier(train_data, train_target, test_data, test_target)
    svm_classifier(train_data, train_target, test_data, test_target)
    nb_classifier(train_data, train_target, test_data, test_target)


if __name__ == "__main__":
    main()