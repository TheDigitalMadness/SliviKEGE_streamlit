import streamlit as st


def get_ans_on_kim(kim_num):
    st.success('start')
    import requests
    import json

    try:
        st.success('try')
        res = requests.get(f'https://kompege.ru/api/v1/variant/kim/{kim_num}')
        st.success('res')
        data = json.loads(res.text)

        st.success('+++')

        tasks = data['tasks']
        answers = []
        index = 1
        for task in tasks:
            try:
                taskId = task['taskId']
            except:
                taskId = 'без номера'
            taskId = str(taskId)
            taskId += ' (' + str(index) + ')'
            taskAnswer = task['key']
            answers.append({'id': taskId, 'answer': str(taskAnswer)})
            index += 1

        return answers

    except:
        return 'Unexpected error'


st.title('Получение ответов на КЕГЭ варианты')
variant_id = st.number_input('Номер варианта', min_value=0, value=12345678, step=1)

if st.button('Получить'):
    answers = get_ans_on_kim(int(variant_id))
    if isinstance(answers, list):
        st.write(answers)
    else:
        st.error(answers)