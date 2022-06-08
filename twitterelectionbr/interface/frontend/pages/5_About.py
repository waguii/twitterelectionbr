import streamlit as st
from static.core_css import main_css
from components.bootstrap import team_card

def custom_css():
    st.markdown("""<style>
.list-inline-item{
    margin: 0px !important;
    padding: 0px !important;
}

.social-link {
    width: 30px;
    height: 30px;
    border: 1px solid #ddd;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #666;
    border-radius: 50%;
    transition: all 0.3s;
    font-size: 0.9rem;
}

.social-link:hover, .social-link:focus {
    background: #ddd;
    text-decoration: none;
    color: #555;
}</style>""", unsafe_allow_html=True)

def main():
    st.markdown("<h1 style='text-align: center; color: white;'>About US</h1>", unsafe_allow_html=True)
    #WRITE THE CODE BELOW

    col1, col2, col3 = st.columns(3)

    with col1:
        team_card("Bulend Karadag",
                  "São Paulo - Brazil",
                  "https://avatars.githubusercontent.com/u/49818918?v=4",
                  "https://www.linkedin.com/in/bulend-karadag-9a3895175/",
                  "https://lewagon-alumni.slack.com/app_redirect?channel=U03ALSW5TC7",
                  "https://github.com/bulend-karadag")

    with col2:
        team_card("Luiza Paiva",
                  "Rio de Janeiro - Brazil",
                  "https://avatars.githubusercontent.com/u/52924196?v=4",
                  "https://www.linkedin.com/in/luiza-paiva-520a9412a/",
                  "https://lewagon-alumni.slack.com/app_redirect?channel=U03BNQ8E67J",
                  "https://github.com/luizasbpaiva")

    with col3:
        team_card("Wagner Sousa",
                  "Campina Grande - Brazil",
                  "https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1649636233/yjgmsd5wpsjqpruunui7.jpg",
                  "https://www.linkedin.com/in/waguii/",
                  "https://lewagon-alumni.slack.com/app_redirect?channel=U03AZ838ZB6",
                  "https://github.com/waguii")


main_css()
custom_css()
main()
