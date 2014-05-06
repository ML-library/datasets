import pandas as pd
import numpy as np

def true_positives(s1, s2):
    """
    The "true positives" are the intersection of the two lists
      s1: true labels
      s2: predicted labels
    """
    return len(set(s1).intersection(s2))

def false_positives(s1, s2):
    """
    false positives are predicted items that aren't real
      s1: true labels
      s2: predicted labels
    """
    return len(set(s1).difference(s2))

def false_negatives(s1, s2):
    """
    false negatives are real items that aren't predicted
      s1: true labels
      s2: predicted labels
    """
    return len(set(s2).difference(s1))

def precision(s1, s2):
    """
    Precision is the ratio of true positives (tp) to all predicted positives (tp + fp)
      s1: true labels
      s2: predicted labels
    """
    tp = true_positives(s1, s2)
    fp = false_positives(s1, s2)
    if tp == 0 and fp == 0:
        return 0.0
    return 1.0 * tp / (tp + fp)

def recall(s1, s2):
    """
    Recall is the ratio of true positives to all actual positives (tp + fn)
      s1: true labels
      s2: predicted labels
    """
    tp = true_positives(s1, s2)
    fn = false_negatives(s1, s2)
    if tp == 0 and fn == 0:
        return 0.0
    return 1.0 * tp / (tp + fn)

def f1(s1, s2):
    """
    The F1 score, commonly used in information retrieval, measures accuracy using the statistics precision (p) and recall (r).
      s1: true labels
      s2: predicted labels
    """
    p = precision(s1, s2)
    r = recall(s1, s2)
    if p == 0 and r == 0:
        return 0.0
    return 2.0 * p * r / (p + r)

def mean_f1(y_true, y_pred):
    sets = zip(y_true, y_pred)
    return sum([f1(s1, s2) for s1, s2 in sets]) / len(sets)

def make_list(df):
    """
    Helper function does something like this:
    
    df = [[1, 0, 0, 0],		
	  [1, 0, 0, 0],
	  [0, 1, 0, 0],		smth = [[1, 2],
	  [0, 1, 0, 0],  ---->		[3, 4, 5],
	  [0, 1, 0, 0],			[6],
	  [0, 0, 1, 0],			[7]]
	  [0, 0, 0, 1]]
	  
    """
    classes = df.shape[1] if len(df.shape) == 2 else 1
    smth = [[] for i in xrange(0, classes)]
    for i in xrange(df.shape[0]):
        # it's like df[i] == 1
        one = np.where(df[i] > 0.1)[0]
        if len(one) == 1:
            smth[one[0]].append(i + 1)
    return smth
 
def calculate_f1(true_inputs, pred_inputs):
    """
    Reads csv's in the folder and computes mean F1 or just F1 if there's only two classes
    """
    trues = np.array(pd.read_csv(true_inputs, header=None), dtype=int)
    pred = np.array(pd.read_csv(pred_inputs, header=None), dtype=int)
    tr_list = make_list(trues)
    pr_list = make_list(pred)
    
    return mean_f1(tr_list, pr_list)
  
if __name__ == '__main__':
    print calculate_f1("test_answers.csv", "pred_answers.csv")
 
