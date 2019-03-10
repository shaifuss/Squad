import decode
import bag_of_words


MAX_PARAGRAPHS = 1000
MAX_QS = 1


if __name__ == '__main__':
    context, q_list = decode.unpack()
    mat = bag_of_words.generate(context[0:MAX_PARAGRAPHS], q_list[0:MAX_QS])

