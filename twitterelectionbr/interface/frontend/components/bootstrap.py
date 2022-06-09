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

def profile_card(profile):
    st.markdown(f"""
                <div class="container mt-4 mb-4 p-3 d-flex justify-content-center">
                    <div class="bg-dark card p-4">
                        <div class=" image d-flex flex-column justify-content-center align-items-center">
                            <button class="btn btn-secondary"> <img src="{profile['profileImageUrl']}" height="100" width="100" /></button> <span class="name mt-3">{profile['displayname']}</span> <span class="idd">@{profile['username']}</span>
                            <div class="d-flex flex-row justify-content-center align-items-center mt-3"> <span class="number">{profile['followersCount']} <span class="follow">Followers</span></span> </div>
                            <div class="d-flex flex-row justify-content-center align-items-center mt-3"> <span class="number">{profile['mediaCount']} <span class="follow">Posts</span></span> </div>
                            <div class="text mt-3"> <span>{profile['description']}</span> </div>
                            <div class=" px-2 rounded mt-4 date "> <span class="join">Joined {profile['created']}</span> </div>
                        </div>
                    </div>
                </div>""", unsafe_allow_html=True)
