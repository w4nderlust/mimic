# mimic

A simple character level language modeling tool.

## Usage

Usage: mimic.py [options]

Options:
  -h, --help            show this help message and exit
  -t TRAIN_PATH, --train=TRAIN_PATH
                        input file / directory for training
  -o ORDER, --order=ORDER
                        order of the model to train
  -m MODEL_PATH, --model=MODEL_PATH
                        file to store the model
  -g GENERATE_PATH, --generate=GENERATE_PATH
                        file to save the generated output
  -l LENGTH, --length=LENGTH
                        length of the generated text
  -n NUMBER_TEXTS, --num=NUMBER_TEXTS
                        number of texts to generate
