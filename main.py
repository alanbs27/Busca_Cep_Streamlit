import requests
import streamlit as st
import base64




st.set_page_config(page_title='Find Cep',
                   page_icon=':compass:',
                   layout='wide'
                   )

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    backgraund: linear-gradient(...);
    background-image: url("https://media.istockphoto.com/photos/cement-shelf-and-floor-on-concrete-background-for-design-picture-id1345203265?b=1&k=20&m=1345203265&s=612x612&w=0&h=u4Vs0oatELuy1jPR8sAVgBeQ6Y-I4x2gjRJCJ6Ra-ZU=");
    background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

def buscar(cep):

    cep = cep.replace('-', '')
    if len(cep) == 8:

        url = f'https://viacep.com.br/ws/{cep}/json/'
        resposta = requests.get(url)
        dict_resposta = resposta.json()
        if resposta.status_code == 200:
            return dict_resposta
        else:
            return None


col1, col2, col3 = st.columns(3)

with col2:

    st.header('🗺 **Buscador de Endereço**')
    st.subheader('Insira o cep para buscar o endereço')
    cep = st.text_input('', max_chars=8, placeholder='Insira aqui')

    if st.button('Buscar'):
        retorno = buscar(cep)
        if retorno is not None:
            st.subheader(f':blue[Cep procurado: {retorno["cep"]}]' )
            st.subheader(f':blue[Endereço: {retorno["logradouro"]}]')
            st.subheader(f':blue[Bairro: {retorno["bairro"]}]')
            st.subheader(f':blue[Cidade: {retorno["localidade"]}]')
            st.subheader(f':blue[UF: {retorno["uf"]}]')




