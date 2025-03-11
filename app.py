import streamlit as st
import pandas as pd


st.markdown(
        """
        <style>
        .stButton>button {
            width: 100%;  /* Ширина кнопки подстраивается под текст */
            padding: 10px 20px;  /* Добавляем отступы для красоты */
        }
        </style>
        """,
        unsafe_allow_html=True
    )


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
            answers.append({'Номер задания': index, 'Номер в базе': taskId, 'Ответ': str(taskAnswer).replace('\\n', ' | ')})
            index += 1

        return answers

    except:
        return 'Unexpected error'


def KegeSlivi():
    st.title('Получение ответов на КЕГЭ варианты')
    variant_id = st.number_input('Номер варианта', min_value=0, value=12345678, step=1)
    
    if st.button('Получить'):
        answers = get_ans_on_kim(int(variant_id))
        if isinstance(answers, list):
            df = pd.DataFrame(answers)
    
            st.dataframe(df, hide_index=True)
        else:
            st.error('Неверный номер варианта')


def RegeSlivi():
    st.title('Разрабатываю')


def DocsSlivi():
    st.title('Планируется в разработке после РешуЕГЭ')


mode = 1

with st.sidebar:
    st.title('Функционал')
    b_kegeSlivi = st.button('Ответы на КЕГЭ')
    b_RegeSlivi = st.button('Ответы на РешуЕГЭ (coming soon)')
    b_docsSlivi = st.button('Ответы на тесты из Google Docs (coming soon)')

    if b_kegeSlivi:
        mode = 1
    elif b_RegeSlivi:
        mode = 2
    elif b_docsSlivi:
        mode = 3


modes_actions = {
    1: KegeSlivi,
    2: RegeSlivi,
    3: DocsSlivi
}

modes_actions[mode]()
