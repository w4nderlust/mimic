'''
    Author: w4nderlust
    License: MIT
'''
from collections import defaultdict, Counter
from random import random
import codecs
from optparse import OptionParser
import cPickle as pickle
import os
import operator


class Model(object):
    def __init__(self, lm, order):
            self.lm = lm
            self.order = order


def get_files(path):
    files = []
    if os.path.isdir(path):
        for file_name in os.listdir(path):
            files.append(os.path.join(path, file_name))
    else:
        files.append(path)
    return files


def normalize(counter):
        s = float(sum(counter.values()))
        return [(c, cnt/s) for c, cnt in counter.iteritems()]


def train_lm(file_path, order=4):
    files = get_files(file_path)
    lm = defaultdict(Counter)
    for f in files:
        text_data = file(f).read()
        padding = "~" * order
        text_data = padding + text_data
        for i in xrange(len(text_data) - order):
            history, char = text_data[i:i + order], text_data[i + order]
            lm[history][char] += 1
    lm = {hist: sorted(normalize(chars),             # sorted -> will be faster
          key=operator.itemgetter(1), reverse=True)  # in generating letters
          for hist, chars in lm.iteritems()}
    return Model(lm, order)


def generate_letter(model, history):
        history = history[-model.order:]
        dist = model.lm[history]
        rand_prob = random()
        for char, prob in dist:
            rand_prob = rand_prob - prob
            if rand_prob <= 0:
                return char


def generate_text(model, n_letters=1000):
    history = "~" * model.order
    out = []
    for i in xrange(n_letters):
        c = generate_letter(model, history)
        history = history[-model.order:] + c
        out.append(c)
    return unicode("".join(out), "utf-8")


def write_to_file(utf8_string, file_name):
    f = codecs.open(file_name, "w", "utf-8")
    f.write(utf8_string)
    f.close()


def main():
    parser = OptionParser()
    parser.add_option("-t", "--train", action="store", dest="train_path",
                            help="input file / directory for training")
    parser.add_option("-o", "--order", action="store", dest="order",
                            type="int", default=4,
                            help="order of the model to train")
    parser.add_option("-m", "--model", action="store", dest="model_path",
                            help="file to store the model")
    parser.add_option("-g", "--generate", action="store", dest="generate_path",
                            help="file to save the generated output")
    parser.add_option("-l", "--length", action="store", dest="length",
                            type="int", default=1000,
                            help="length of the generated text")
    parser.add_option("-n", "--num", action="store", dest="number_texts",
                            type="int", default=1,
                            help="number of texts to generate")
    (options, args) = parser.parse_args()
    model = None
    if options.train:
        if options.input_path:
            print "Training model from path: " + options.input_path
            model = train_lm(options.input_path, options.order)
            print "Finished training"
            if (options.model_path):
                print "Saving model to: " + options.model_path
                with open(options.model_path, "wb") as model_file:
                    pickle.dump(model, model_file, pickle.HIGHEST_PROTOCOL)
                print "Finished saving"
            else:
                print "The trained model will not be saved"
                print "  (to save it use -m option)"
        else:
            print "Add in input path with -i option"
    if options.generate_path:
        if not model:
            if options.model_path:
                print "Loading model from path: " + options.model_path
                with open(options.model_path, 'rb') as model_file:
                    model = pickle.load(model_file)
                print "Finished loading"
            else:
                print "Add the model's path with -m option"
        if model:
            if options.number_texts == 1:
                print "Generating text"
                text = generate_text(model, options.length)
                print "Saving text to: " + options.generate_path
                write_to_file(text, options.generate_path)
            else:
                for i in xrange(options.number_texts):
                    print "Generating text " + str(i + 1)
                    text = generate_text(model, options.length)
                    splits = options.generate_path.split(".")
                    if (len(splits) > 1):
                        path = (".".join(splits[:-1]) + "_" + str(i + 1) +
                                "." + splits[-1])
                    else:
                        path = options.generate_path + "_" + str(i + 1)
                    print "Saving text to: " + path
                    write_to_file(text, path)
            print "Finished saving"


if __name__ == "__main__":
    main()
