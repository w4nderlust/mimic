# mimic

A simple character level language modeling tool.

## Usage

Usage: mimic.py [options]

Options:

-  -h, --help            show this help message and exit
-  -t TRAIN_PATH, --train=TRAIN_PATH
                        input file / directory for training
-  -o ORDER, --order=ORDER
                        order of the model to train
-  -m MODEL_PATH, --model=MODEL_PATH
                        file to store the model
-  -g GENERATE_PATH, --generate=GENERATE_PATH
                        file to save the generated output
-  -l LENGTH, --length=LENGTH
                        length of the generated text
-  -n NUMBER_TEXTS, --num=NUMBER_TEXTS
                        number of texts to generate

### Example

- Download The King James Version of the Bible in text format encoded in UTF-8 from Project Gutenberg: http://www.gutenberg.org/ebooks/10
- Split the text in chapters/books (I used csplit)
- Train a model of order 15: python mimic.py -t bible_chapters/ -o 15 -m bible_model
- Generate a text with the trained model: python mimic.py bible_model -g bible_generated.txt

This is an example of what you can get:

> The First Epistle of Paul the Apostle to Titus
>
> Paul, a servant of Christ.
> But we were gentle among you, even as a nurse cherisheth her children: So being affectionately desirous of you, we were willing to have imparted unto you, not the gospel of Christ.
> But though we, or an angel from heaven, as the voice of thy cry; when he shall let your children tell their children, and those that were born unto them, That the sons of God shouted for joy?
