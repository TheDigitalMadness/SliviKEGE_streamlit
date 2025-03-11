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
            answers.append({'Номер задания': index, 'Номер в базе': taskId, 'Ответ': str(taskAnswer)})
            index += 1

        return answers

    except:
        return 'Unexpected error'


st.title('Получение ответов на КЕГЭ варианты')
variant_id = st.number_input('Номер варианта', min_value=0, value=12345678, step=1)

if st.button('Получить'):
    answers = [
        {"Номер задания": 1, "Номер в базе": "10715", "Ответ": "11"},
        {"Номер задания": 2, "Номер в базе": "13829", "Ответ": "1548420"},
        {"Номер задания": 3, "Номер в базе": "5923", "Ответ": "80"},
        {"Номер задания": 4, "Номер в базе": "1130", "Ответ": "32804"},
        {"Номер задания": 5, "Номер в базе": "6089", "Ответ": "11 1416"},
        {"Номер задания": 6, "Номер в базе": "2215", "Ответ": "2407 1271"},
        {"Номер задания": 7, "Номер в базе": "676", "Ответ": "18"},
        {"Номер задания": 8, "Номер в базе": "без номера", "Ответ": "17"},
        {"Номер задания": 9, "Номер в базе": "без номера", "Ответ": "28 31"},
        {"Номер задания": 10, "Номер в базе": "4795", "Ответ": "35"},
        {"Номер задания": 11, "Номер в базе": "1139", "Ответ": "20"}
    ]

    # Создаем DataFrame
    df = pd.DataFrame(answers)

    # CSS для выравнивания
    st.markdown(
        """
        <style>
        /* Выравнивание заголовков по центру */
        .stDataFrame th {
            text-align: center !important;
        }
        /* Выравнивание текста в ячейках по левому краю */
        .stDataFrame td {
            text-align: left !important;
        }
        .stDataFrame th, .stDataFrame td {
            min-width: 100px !important;
            max-width: 200px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Выводим DataFrame
    st.dataframe(df, hide_index=True)

    
    answers = get_ans_on_kim(int(variant_id))
    if isinstance(answers, list):
        st.write(answers)
        for ans in answers:
            st.success(f'{ans["id"]}:')
            st.write(f'{ans["answer"]}')
    else:
        st.error('Неверный номер варианта')
