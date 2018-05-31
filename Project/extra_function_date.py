import matplotlib.pyplot as plt
import numpy as np
import itertools

def juliandate(pythondt):
    """
    Returns the julian date from a python datetime object
    """

    # year = int(year)
    # month = int(month)
    # day = int(day)

    year = int(pythondt.strftime("%Y"))
    month = int(pythondt.strftime("%m"))
    day = int(pythondt.strftime("%d"))

    hours = int(pythondt.strftime("%H"))
    minutes = int(pythondt.strftime("%M"))
    seconds = int(pythondt.strftime("%S"))

    fracday = float(hours + float(minutes) / 60.0 + float(seconds) / 3600.0) / 24.0
    # fracday = 0

    # First method, from the python date module. It was wrong, I had to subtract 0.5 ...
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    jd1 = day + ((153 * m + 2) // 5) + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    jd1 = jd1 + fracday - 0.5

    # Second method (I think I got this one from Fundamentals of Astronomy)
    # Here the funny -0.5 was part of the game.

    j1 = 367 * year - int(7 * (year + int((month + 9) / 12)) / 4)
    j2 = -int((3 * ((year + int((month - 9) / 7)) / 100 + 1)) / 4)
    j3 = int(275 * month / 9) + day + 1721029 - 0.5
    jd2 = j1 + j2 + j3 + fracday

    # print "Date: %s" % pythondt.strftime("%Y %m %d  %H:%M:%S")
    # print "jd1 : %f" % jd1
    # print "jd2 : %f" % jd2

    # This never happened...
    if abs(jd1 - jd2) > 0.00001:
        print("ERROR : julian dates algorithms do not agree...")
        sys.exit(1)

    return jd2


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    # plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')