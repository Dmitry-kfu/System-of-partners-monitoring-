#!/usr/bin/env python
# coding: utf-8


import pickle
import streamlit as st
import pandas as pd



st.title('Аналитический модуль системы информационного мониторинга контрагентов Банка')




st.sidebar.header('Параметры финансовой отчетности')





def user_input_features():
        VNActive = st.sidebar.number_input('VNActive', min_value =0, max_value =5000000000000,  step=10000, value=0)
        OActive =st.sidebar.number_input('OActive', min_value =0, max_value =5000000000000,  step=10000, value=0)
        VBalance = st.sidebar.number_input('VBalance', min_value =0, max_value =10000000000000,  step=10000, value=0)
        YK = st.sidebar.number_input('YK', min_value =0, max_value =5000000000000,  step=10000, value=0)
        CapitalRez=st.sidebar.number_input('CapitalRez', min_value =-100000000000, max_value =10000000000000,  step=100000, value=0)
        LongDebts=st.sidebar.number_input('LongDebts', min_value =0, max_value =10000000000000,  step=10000, value=0)
        ShortTDebts = st.sidebar.number_input('ShortTDebts', min_value =0, max_value = 10000000000000,  step=10000, value=0)
        Revenue = st.sidebar.number_input('Revenue', min_value =0 , max_value =10000000000000,  step=10000, value=0)
        Profit = st.sidebar.number_input('Profit', min_value =-10000000000, max_value =10000000000000,  step=10000, value=0)
        data = {'2020, Внеоборотные активы, RUB':[VNActive],
                                '2020, Оборотные активы, RUB':[OActive],
                                '2020, Активы всего, RUB':[VBalance], 
                                '2020, Уставный капитал , RUB':[YK],
                                '2020, Капитал и резервы, RUB':[CapitalRez],
                                '2020, Долгосрочные обязательства, RUB':[LongDebts],
                                '2020, Краткосрочные обязательства, RUB':[ShortTDebts],
                                '2020, Выручка, RUB':[Revenue],
                                '2020, Чистая прибыль (убыток), RUB':[Profit]}
        features = pd.DataFrame(data, index=[0])
        return features



df = user_input_features()


st.sidebar.header('Показатели для расчета индекса Альтмана и Таффлера')
Zaem = st.sidebar.number_input('Borrowed funds', min_value =0 , max_value =10000000000000,  step=10000, value=0, )
CreditorDebt = st.sidebar.number_input('creditor debt', min_value =0 , max_value =10000000000000,  step=10000, value=0, )
SalesProfit = st.sidebar.number_input('Sales Profit', min_value =-100000000000000 , max_value =10000000000000,  step=10000, value=0)
st.sidebar.header('Реестры банкротов и РНП')
Bancrot = st.sidebar.selectbox("Реестр банкротов: ", ('Да', 'Нет'))
RNP = st.sidebar.selectbox("Реестр недобросовестых поставщиков: ", ('Да', 'Нет'))



st.subheader('Таблица данных для анализа')
st.write(df)



with open('forestbezssch2.pickle', 'rb') as f:
    model_new = pickle.load(f)


prediction = model_new.predict(df)
print(prediction)



LongDebts = df['2020, Долгосрочные обязательства, RUB'].values
CapitalRez = df['2020, Капитал и резервы, RUB'].values
VBalance = df['2020, Активы всего, RUB'].values
VNActive = df['2020, Внеоборотные активы, RUB'].values
OActive = df['2020, Оборотные активы, RUB'].values
ShortTDebts = df['2020, Краткосрочные обязательства, RUB'].values
Revenue = df['2020, Выручка, RUB'].values




AltmanIndex = -0.3877 - 1.0736 * (OActive / (Zaem + CreditorDebt)) + 0.0579 * ((LongDebts + ShortTDebts) / CapitalRez)
TafflerIndex = 0.53 * (SalesProfit / ShortTDebts) + 0.13 * (OActive / (LongDebts + ShortTDebts)) + 0.18 * (ShortTDebts / VBalance) + \
                   0.16 * (Revenue / VBalance)



st.subheader('Индекс Альтмана (нормативное значение меньше 0)')
st.write(AltmanIndex)


st.subheader('Индекс Таффлера (нормативное значение более 0,3)')
st.write(TafflerIndex)

st.subheader('Реестр банкротов')
st.write(Bancrot)

st.subheader('РНП')
st.write(RNP)


st.subheader('Прогноз риска сотрудничества на основе финансовых показателей компании')



if prediction==1:
    st.write('Высокий риск, обратите внимание на индексы, реестры и финансовые показатели')
elif df.values.any()==0:
    st.write('Высокий риск, обратите внимание на индексы, реестры и финансовые показатели')
elif AltmanIndex>0:
    st.write('Высокий риск, обратите внимание на индексы, ресстры и финансовые показатели')
elif AltmanIndex==0:
    st.write('Высокий риск, обратите внимание на индексы, реестры и финансовые показатели')
elif TafflerIndex<0.3:
    st.write('Высокий риск, обратите внимание на индексы, реестры и финансовые показатели')
elif Bancrot =='Да':
    st.write('Высокий риск, обратите внимание на индексы, реестры и финансовые показатели')
elif RNP =='Да':
    st.write('Высокий риск, обратите внимание на индексы, реестры и финансовые показатели')
else:
    st.write('Риск низкий, сотрудничество возможно')






