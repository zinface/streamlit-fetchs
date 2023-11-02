import streamlit as st 
import requests
import os

def _max_width_(prcnt_width:int = 75):
    max_width_str = f"max-width: {prcnt_width}rem;"
    st.markdown(f""" 
                <style> 
                .block-container{{{max_width_str}}}
                </style>    
                """, 
                unsafe_allow_html=True,
    )
_max_width_(80)

# title
st.title('Welcome Streamlit MainPage')

# urls: from https://api.gmit.vip/#/
movies = [
    'https://cache.gumengya.com/index/video/1.mp4', # 3.0M
    'https://cache.gumengya.com/index/video/2.mp4', # 15M
    'https://cache.gumengya.com/index/video/3.mp4', # 4.1M
    'https://cache.gumengya.com/index/video/4.mp4', # 
    'https://cache.gumengya.com/index/video/5.mp4', # 992k
    'https://cache.gumengya.com/index/video/6.mp4', # 
    'https://cache.gumengya.com/index/video/7.mp4', # 3.5M
    'https://cache.gumengya.com/index/video/8.mp4', # 29M
    # No More
]

# feat: use streamlit session state save 'movies_index' value 
if 'movies_index' not in st.session_state.keys():
    st.session_state['movies_index'] = 0
else:
    st.session_state['movies_index'] += 1
    if st.session_state['movies_index'] >= len(movies):
        st.session_state['movies_index'] = 0

# feat: movie url index
movies_index = st.session_state['movies_index']


# 0. only image
# st.image('./assets/screenshot.png')


@st.cache_data
def get_video(url):
    if not os.path.exists('assets/movies'):
        os.mkdir('assets/movies')

    filename = os.path.basename(url)
    filepath = f'assets/movies/{filename}'
        
    if not os.path.exists(filepath):
        video_data = requests.get(url).content
        if len(video_data):
            with open(filepath, 'wb') as f:
                f.write(video_data)

    with open(filepath, 'rb') as f:
        return f.read()
    
# 1. use get_video + (streamlit cache data) + (save video to local)
# st.video(get_video(movies[movies_index]))


# 2. use markdown + html + autoplay
# st.markdown(f'''
# <div class="intro-video view" id="home"> 
#     <div id="container">
#         <video id="background_video" class="main st-emotion-cache-uf99v8 ea3mdgi5" webkit-playsinline="true" x-webkit-airplay="true" playsinline="true" x5-video-player-type="h5" x5-video-player-fullscreen="true" x5-video-orientation="h5" preload="" airplay="allow" muted="muted" loop="" autoplay="">抱歉，您的浏览器不支持内嵌视频<source src="https://cache.gumengya.com/index/video/8.mp4" type="video/mp4"></video>
#     </div>
# </div>
# <script type="text/javascript" src="https://cache.gumengya.com/api/js/APlayer.min.js"></script>
# ''', unsafe_allow_html=True)



# 3. simple markdown + html + autoplay
# st.markdown(f'<video id="background_video" class="main st-emotion-cache-uf99v8 ea3mdgi5" webkit-playsinline="true" x-webkit-airplay="true" playsinline="true" x5-video-player-type="h5" x5-video-player-fullscreen="true" x5-video-orientation="h5" preload="" airplay="allow" muted="muted" loop="" autoplay="">抱歉，您的浏览器不支持内嵌视频<source src="{movies[movies_index]}" type="video/mp4"></video>', unsafe_allow_html=True)


# 4. simple st.video + url 
st.video(movies[movies_index]) # not autoplay

# : view movie source url
st.text('source: ' + movies[movies_index])