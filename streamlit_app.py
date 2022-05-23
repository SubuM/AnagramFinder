
import streamlit as st
import streamlit_authenticator as stauth
from itertools import permutations,combinations
import enchant


def checkAngrm():
    d = enchant.Dict('en_US')
    word = st.text_input('Enter your word:', placeholder='Enter your jumbled word')
    letters = [chr for chr in word]
    repeat_check = []
    word_len = len(word)

    for number in range(word_len, len(letters) + 1):  # For Loop
        for current_set in combinations(letters, number):  # Combinations Function
            # Code for the Basic Anagram Finder
            for current in permutations(current_set):
                current_word = ''.join(current)
                if d.check(current_word) and current_word not in repeat_check:
                    st.write(current_word)
                    repeat_check.append(current_word)


def usrAuth():
    st.set_page_config(page_title='Anagram Solver', page_icon='random', initial_sidebar_state='auto')
    st.sidebar.image('./images/anagram.png')
    
    # hide hamburger menu and footer
    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden}
                    footer {visibility: hidden}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    names = ['Subho', 'Radha', 'Babu', 'Rimi']
    usernames = ['subu', 'liti', 'gullu', 'rimi']
    passwords = ['Bubun11$', 'Gullu11$', 'Gullu11$', 'Rimi']

    hashed_passwords = stauth.hasher(passwords).generate()

    authenticator = stauth.authenticate(names, usernames, hashed_passwords, 'ST_cookie', 'ST_sign_key',
                                        cookie_expiry_days=30)

    name, authentication_status = authenticator.login('Login', 'main')

    if st.session_state['authentication_status']:
        st.success('Welcome *%s*' % (st.session_state['name']))
        checkAngrm()
    elif st.session_state['authentication_status'] == False:
        st.error('Username/Password is incorrect')
    elif st.session_state['authentication_status'] == None:
        st.error('Please enter your username and password')


if __name__ == '__main__':
    usrAuth()
