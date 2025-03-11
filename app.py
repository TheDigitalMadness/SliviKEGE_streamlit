import streamlit as st
import pandas as pd


def get_ans_on_kim(kim_num):
    import requests
    import json

    try:
        res = requests.get(f'https://kompege.ru/api/v1/variant/kim/{kim_num}')
        data = json.loads(res.text)

        tasks = data['tasks']
        answers = []
        index = 1
        for task in tasks:
            try:
                taskId = task['taskId']
            except:
                taskId = 'без номера'
            taskId = str(taskId)
            taskAnswer = task['key']
            answers.append({'Номер задания': index, 'Номер в базе': taskId, 'Ответ': str(taskAnswer).replace('\\n', '\n')})
            index += 1

        return answers

    except:
        return 'Unexpected error'


st.title('Получение ответов на КЕГЭ варианты')
variant_id = st.number_input('Номер варианта', min_value=0, value=12345678, step=1)

if st.button('Получить'):
    answers = get_ans_on_kim(int(variant_id))
    if isinstance(answers, list):
        df = pd.DataFrame(answers)

        st.dataframe(df, hide_index=True)
    else:
        st.error('Неверный номер варианта')
