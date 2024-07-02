# import streamlit as st
#
# col1, col2 = st.columns(2)
#
# with col1:
#     st.image("images/photo.png")

string1 = "The weather is sunny in SC. The weather is cloudy. the weather"
word=""
list =[]
count =0
for i in string1:
    if i=="." or i=="," or i=="!" or i=="?" or i==";":
        continue
    if i ==" ":
        list.append(word)
        word=""
    else:
        word=word+i


for i in list:
    

print(list)







print(list)
