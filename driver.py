"""

"""


import decode
import sys
import bag_of_words as bow


MAX_PARAGRAPHS = 5
MAX_QS = 1


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] != 'dev-v2.0.json':
        raise Exception('Usage: driver dev-v2.0.json')

    # create lists of paragraphs and questions
    context, q_list = decode.unpack(sys.argv[1])
    # retrieve index of most like paragraph
    index = bow.find_paragraph(bow.generate(context[0:MAX_PARAGRAPHS], q_list[0:MAX_QS]))
    print('The answer most likely can be found in the following paragraph', context[index], sep="\n")


