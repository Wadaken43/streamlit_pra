import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

latest_itererion = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_itererion.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'

st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ')
expander3.write('問い合わせ3の回答')


# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 20)

# 'あなたの趣味:', text
# 'コンディション：', condition


# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、',option, 'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='犬っこ', use_column_width=True) 


