import json


def unpack():
    with open('C:\\Users\\Harriet\\PycharmProjects\\Squad\\dev-v2.0.json') as jfile:
        dataset = json.load(jfile)
        context = []
        qas = []
        for i in range(len(dataset['data'])):   # for each article
            temp = dataset['data'][i]['paragraphs']
            for j in range(len(temp)):          # for each paragraph in given article
                context.append((temp[j]['context']))
                qas.append((temp[j]['qas']))
        # filter out questions
        q_list = []
        for i in range(len(qas)):
            temp = qas[i]
            for j in range(len(temp)):
                q_list.append(temp[j]['question'])

    return context, q_list







