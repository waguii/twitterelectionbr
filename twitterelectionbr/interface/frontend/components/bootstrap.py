import streamlit as st

def card(title, text, image):
    st.markdown("""
                <div class="card" style="width: 18rem;">
                    <img class="card-img-top" src="{image}" alt="Card image cap">
                        <div class="card-body">
                            <h5 class="card-title">{title}</h5>
                            <p class="card-text">{text}</p>
                            <a href="#" class="btn btn-primary">Go somewhere</a>
                        </div>
                    </div>""",
    unsafe_allow_html=True)

def team_card(name, location, image_url, linkedin, slack, github):
    st.markdown(f"""
                 <div class="bg-dark rounded shadow-sm py-5 px-4 text-center">
                 <img src="{image_url}" alt="" width="100" class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm">
                <h5 class="mb-0">{name}</h5><span class="small text-uppercase text-muted">{location}</span>
                <ul class="social mb-0 list-inline mt-3">
                    <li class="list-inline-item"><a href="{slack}" class="social-link"><i class="fa fa-slack"></i></a></li>
                    <li class="list-inline-item"><a href="{github}" class="social-link"><i class="fa fa-github"></i></a></li>
                    <li class="list-inline-item"><a href="{linkedin}" class="social-link"><i class="fa fa-linkedin"></i></a></li>
                </ul>
            </div>""",
    unsafe_allow_html=True)
