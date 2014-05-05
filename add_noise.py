#!/usr/bin/python2
import pandas as pd
import numpy as np
import os.path
import sys


def usage():
    print """./add_noise.py <answers file> <output answers with noise> <percentage of noise>
    answers file: path to CSV file
    output answers with noise: path to CSV file
    percentage of noise: number from 0 to 100"""


def check_input(answers_file, output_file, percentage):
    result = True
    if not os.path.isfile(answers_file):
        print "File {0} doesn't exists".format(answers_file)
        result = False
    if not os.path.exists(os.path.dirname(output_file)):
        print "Directory {0} doesn't exists".format(os.path.dirname(output_file))
        result = False
    if not percentage.isdigit() or not (0 <= int(percentage) <= 100):
        print "Number from 0 to 100 expected but '{0}' found".format(percentage)
        result = False
    return result


def main():
    if len(sys.argv) != 4 or not check_input(*(sys.argv[1:])):
        usage()
        return

    answers_file = sys.argv[1]
    output_file = sys.argv[2]
    percentage = int(sys.argv[3])

    answers = np.array(pd.read_csv(answers_file, header=None), dtype=int)
    m = answers.shape[0]
    n = answers.shape[1]
    noised_count = int(m * percentage / 100.0)
    to_be_noised = np.arange(m)
    np.random.shuffle(to_be_noised)
    to_be_noised = to_be_noised[:noised_count]
    for i in to_be_noised:
        if n == 1:
            answers[i][0] ^= 1
        else:
            # it's like answers[i] == 1
            one = np.where(answers[i] > 0.1)[0]
            if len(one) != 1:
                print "Bad format: in line {0}".format(i)
                return
            ans = one[0]
            answers[i][ans] = 0
            variants = np.delete(np.arange(n), ans)
            np.random.shuffle(variants)
            new_ans = variants[0]
            answers[i][new_ans] = 1

    try:
        np.savetxt(output_file, answers, fmt="%d", delimiter=",")
        print "File {0} saved".format(output_file)
    except IOError:
        pass


if __name__ == "__main__":
    main()