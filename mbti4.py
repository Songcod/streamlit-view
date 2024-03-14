import streamlit as st
import pandas as pd
import numpy as np

# CSS 스타일을 추가하는 함수
def local_css(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:  # 파일을 열 때 encoding을 UTF-8로 지정
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        

def set_page_style():
    st.markdown("""
    <style>
    /* Adjust button style for initial state and hover */
    .stButton>button {
        border: 2px solid rgb(0, 0, 0); /* Black border */
        background-color: transparent; /* Transparent background */
        color: rgb(0, 0, 0); /* Black text */
        padding: 10px 24px; /* Padding */
        border-radius: 20px; /* Rounded corners */
        font-size: 16px; /* Font size */
        transition: background-color 0.3s, color 0.3s; /* Smooth transition for background and text color */
        display: inline-block; /* Necessary for centering */
        margin: 0 auto; /* Center button */
        width: fit-content; /* Adjust width to content */
    }
    .stButton>button:hover {
        background-color: rgb(17, 230, 216); /* Change background color on hover */
        color: white; /* Change text color on hover */
    }

    /* Center align images */
    .stImage > img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%; /* Adjust the width as needed */
    }
    
    /* Ensure all text is centered */
    .markdown-text-container, .stMarkdown {
        text-align: center !important;
    }
    </style>
    """, unsafe_allow_html=True)



# def set_page_style():
#     st.markdown("""
#         <style>
#         /* 중앙 정렬을 위한 CSS 적용 */
#         .stRadio > div, .stButton > button {
#             display: flex;
#             justify-content: center;
#             margin: auto;
#             width: auto; /* 버튼의 너비를 내용에 맞게 조정 */
#         }
        
#         /* 버튼 스타일 조정 */
#         .stButton>button {
#             min-height: 46px; /* 버튼의 최소 높이 */
#             font-size: 18px; /* 버튼 내 텍스트 크기 */
#             border: 1px solid rgb(225, 225, 225);
#             background-color: rgb(255, 255, 255);
#             color: rgb(0, 0, 0);
#             border-radius: 20px; /* 버튼 모서리 둥글게 */
#             padding: 0 25px; /* 버튼 내부 여백 */
#             cursor: pointer; /* 마우스 오버 시 커서 변경 */
#             transition: all 0.3s ease; /* 부드러운 색상 전환 효과 */
#         }

#         .stButton>button:hover {
#             border-color: rgb(17, 230, 216); /* 호버 시 테두리 색상 변경 */
#             background-color: rgb(17, 230, 216); /* 호버 시 배경 색상 변경 */
#             color: white; /* 호버 시 텍스트 색상 변경 */
#         }

#         /* 설문 질문 및 옵션 스타일 조정 */
#         .stMarkdown {
#             text-align: center; /* 텍스트 중앙 정렬 */
#         }

#         .stRadio > div {
#             display: flex;
#             flex-direction: column;
#             align-items: center; /* 세로 축 중앙 정렬 */
#         }

#         /* 설문 옵션 텍스트 크기 조정 */
#         label {
#             font-size: 30px; /* 라벨(설문 옵션)의 텍스트 크기 */
#         }
                
#         /* 선택지 스타일 */
#         .stRadio > div > label {
#             color: rgb(0, 0, 0); /* 텍스트 색상 */
#             background-color: rgba(255, 255, 255, 0.6); /* 배경색 */
#             padding: 10px; /* 패딩 */
#             margin-bottom: 8px; /* 선택지 사이의 마진 */
#             border-radius: 10px; /* 모서리 둥글기 */
#             border: 1px solid rgb(0, 0, 0); /* 테두리 */
#             display: block; /* 블록 레벨 요소로 표시 */
#             width: 100%; /* 최대 너비 */
#             box-sizing: border-box; /* 박스 크기 계산 방식 */
#         }

#         /* 선택지를 감싸는 div에 대한 스타일 */
#         .stRadio > div {
#             width: 100%; /* 최대 너비 설정 */
#             max-width: 500px; /* 최대 너비를 500px로 제한 */
#             margin: auto; /* 자동 마진으로 중앙 정렬 */
#         }

#         /* 선택지에 마우스 호버 효과 */
#         .stRadio > div > label:hover {
#             background-color: rgba(255, 255, 255, 0.8);
#         }

#         /* 버튼 호버 스타일 */
#         .stButton>button:hover {
#             border-color: rgb(17, 230, 216); /* 호버 시 테두리 색상 변경 */
#             background-color: rgb(17, 230, 216); /* 호버 시 배경 색상 변경 */
#             color: white; /* 호버 시 텍스트 색상 변경 */
#         }
#         </style>
#         """, unsafe_allow_html=True)



# 표지 페이지 스타일 설정 함수
def set_cover_style():
    st.markdown("""
    <style>
    /* 전체 배경색 변경 */
    body {
        background-color: #FFF; /* 밝은 배경으로 설정 */
    }
    
    /* 표지 제목 스타일 */
    h1 {
        color: #111; /* 어두운 글씨 색상 */
        font-size: 36px; /* 제목 크기 */
        text-align: center; /* 중앙 정렬 */
    }
    
    /* 표지 부제목 스타일 */
    .intro-step_game-intro-text__Trjq_ {
        color: #333; /* 부제목 글씨 색상 */
        font-size: 20px; /* 글씨 크기 */
        text-align: center; /* 중앙 정렬 */
        margin-top: 10px; /* 상단 여백 */
    }
    
    /* Streamlit 버튼 전역 스타일 조정 */
    .stButton>button {
        border: none !important; /* 테두리 제거 */
        background-color: rgb(17, 230, 216) !important; /* 버튼 배경색 */
        color: #FFF !important; /* 버튼 글자색 */
        padding: 15px 30px !important; /* 패딩 조정으로 버튼 크기 증가 */
        border-radius: 30px !important; /* 버튼 모서리 둥글게 */
        font-size: 20px !important; /* 글자 크기 */
        display: block !important; /* 블록 디스플레이로 변경 */
        width: fit-content !important; /* 내용에 맞게 너비 조정 */
        margin: 20px auto !important; /* 상하 여백 20px, 좌우 마진 자동으로 중앙 정렬 */
    }
    
    /* SNS 공유 버튼 스타일 */
    .btn-share {
        display: inline-block; /* 인라인 블록으로 표시 */
        width: 40px; /* 너비 */
        height: 40px; /* 높이 */
        background-size: cover; /* 배경 이미지 크기 조절 */
        margin-right: 10px; /* 우측 여백 */
        border-radius: 50%; /* 원형으로 표시 */
    }
    
    /* 설문 결과 스타일 */
    .mostType_result-box__3mRKI {
        margin-top: 30px; /* 상단 여백 */
    }
    
    .mostType_label-bottom__1AKzj {
        display: block; /* 블록으로 표시 */
        text-align: center; /* 중앙 정렬 */
        color: #333; /* 글씨 색상 */
        font-size: 18px; /* 글씨 크기 */
        margin-top: 10px; /* 상단 여백 */
    }
    
    </style>
    """, unsafe_allow_html=True)


# 결과 페이지 스타일 설정 함수
def set_results_style():
    st.markdown("""
    <style>
    body {
        background-color: #F0E68C;
    }
    /* Reuse the button styles from set_page_style for consistency */
    .stButton>button {
        border: 2px solid rgb(0, 0, 0); /* Black border */
        background-color: transparent; /* Transparent background */
        color: rgb(0, 0, 0); /* Black text */
        padding: 10px 24px; /* Padding */
        border-radius: 20px; /* Rounded corners */
        font-size: 16px; /* Font size */
        transition: background-color 0.3s, color 0.3s; /* Transition effect */
        display: inline-block; /* For centering */
        margin: 0 auto; /* Center button */
        width: fit-content; /* Adjust width to content */
    }
    .stButton>button:hover {
        background-color: rgb(17, 230, 216); /* Change background color on hover */
        color: white; /* Change text color on hover */
    }
    </style>
    """, unsafe_allow_html=True)



# 페이지 설정 및 CSS 스타일 적용
st.set_page_config(page_title="옷BTI 테스트", layout="wide")

questions = [
    ("‘오늘부터 단 7일! 고객님만을 위한 특별 할인 쿠폰!’ 카톡이 울렸다. 이때 나의선택은?", 
     ["옷을 살 생각은 없었지만 세일을 한다고 하니 일단 구경한다.", 
      "딱히 옷을 사려고 생각하지 않았으니 무시한다."], 
      "https://cdn.metavv.com/prod/uploads/10749482/images/168542440895775.png"),
    ("앗! 쿠폰이 오늘 사라져요! 고객님이 보유하신 쿠폰이 오늘 만료될 예정입니다.", 
     ["엇!! 내가 호옥시나 필요한 옷이 있을 수도 있으니 12시가 되기 전까지 시간될 때마다 웹서핑을 계속한다.", 
      "에이, 저번 달에도 세일 때문에 샀다가 안 입는 옷들이 있는데 안 사!!", 
      "이런 타임 어택으로 옷을 사면 실패하거나 충동 구매할 확률이 높으니 다음 기회에!"], 
     "https://cdn.metavv.com/prod/uploads/10749482/images/168542440895775.png"),
    ("옷장을 열어보니... 분명히 옷은 많은데 입을 게 없다. 결심한 김에 오늘 하루!! 옷장 정리를 하기로 마음을 먹었는데 생각보다 올해 안 입은 옷이 많다.", 
     ["에이... 언젠간 입겠지. 버리긴 아까우니 입을 일이 있을 때까지 기다린다.", 
      "인별 보니깐 헌옷수거하고 돈으로 돌려주기도 하던데 에잇! 귀찮아!! 바로 헌옷 수거함으로!!",
      "난 안 입지만 괜찮은 옷들인데... 버리긴 아깝고 좋은 곳에 기부해서 재사용할 수 있도록 해야 겠다!"
      ], 
     "https://cdn.metavv.com/prod/uploads/10749482/images/168542440895775.png"),
    ("둘 중 하나를 구매해야 한다면?", 
     ["가성비도 좋고 디자인도 이쁘지만 올해 밖에 못 입을 것 같은 A사 니트", 
      "당장 유행은 아니지만 그래도 오래 입을 수 있는 B사 니트"], 
     "https://cdn.metavv.com/prod/uploads/10749482/images/168542440895775.png"),
    ("오늘은 개강 첫 주! 아쉽게도 이번 학기는 공강이 없는데,,,", 
     ["누가 며칠 전에 입은 걸 알아보면 어떡해!! 매일매일 다른 옷을 입고 나가 나의 패션 센스를 자랑한다.", 
      "에이! 내 옷을 누가 알아본다고!! 적당히 돌려 입는다."], 
     "https://cdn.metavv.com/prod/uploads/10749482/images/168542440895775.png")
]

score_dict = {
    #1
    "옷을 살 생각은 없었지만 세일을 한다고 하니 일단 구경한다." : 2, 
    "딱히 옷을 사려고 생각하지 않았으니 무시한다." : 0,
    # 2
    "엇!! 내가 호옥시나 필요한 옷이 있을 수도 있으니 12시가 되기 전까지 시간될 때마다 웹서핑을 계속한다." : 2, 
    "에이, 저번 달에도 세일 때문에 샀다가 안 입는 옷들이 있는데 안 사!!" : 1, 
    "이런 타임 어택으로 옷을 사면 실패하거나 충동 구매할 확률이 높으니 다음 기회에!" : 0, 
    # 3
    "에이... 언젠간 입겠지. 버리긴 아까우니 입을 일이 있을 때까지 기다린다." : 2, 
    "인별 보니깐 헌옷수거하고 돈으로 돌려주기도 하던데 에잇! 귀찮아!! 바로 헌옷 수거함으로!!" : 1,
    "난 안 입지만 괜찮은 옷들인데... 버리긴 아깝고 좋은 곳에 기부해서 재사용할 수 있도록 해야 겠다!" : 0, 
    # 4
    "가성비도 좋고 디자인도 이쁘지만 올해 밖에 못 입을 것 같은 A사 니트" : 2, 
    "당장 유행은 아니지만 그래도 오래 입을 수 있는 B사 니트" : 0, 
    # 5
    "누가 며칠 전에 입은 걸 알아보면 어떡해!! 매일매일 다른 옷을 입고 나가 나의 패션 센스를 자랑한다." : 2, 
    "에이! 내 옷을 누가 알아본다고!! 적당히 돌려 입는다." : 0
    }

# Find the maximum number of options in any question
max_options = max(len(options) for _, options, _ in questions)

# Initialize or update the response tracker
if 'response_tracker' not in st.session_state:
    st.session_state['response_tracker'] = pd.DataFrame(0, 
                                                        index=np.arange(len(questions)), 
                                                        columns=[f"Option {i+1}" for i in range(max_options)])
    st.session_state['page'] = 'cover' # 현재 cover 페이지에 있다고 설정
    st.session_state['question_index'] = 0 # 첫 질문부터 시작
    st.session_state['selected_options'] = [] # 아직 옵션 선택 부분을 빈칸으로

# Function to display cover page
def display_cover():
    # Apply the cover page styles
    set_cover_style()
    
    # 표지 페이지 HTML 콘텐츠와 스타일 직접 삽입
    st.markdown("""
    <div style="text-align: center;">
        <img src="https://cdn.metavv.com/prod/uploads/10749482/images/168542440895775.png" style="min-height:24rem; max-width: 100%;" alt="">
        <h2 style="color: #111; font-size: 36px;">도파민 중독 테스트</h2>
        <div style="color: #333; font-size: 20px; margin-top: 10px;">내 안의 혈중 도파민 농도는?</div>
        <!-- 버튼 디자인을 HTML로 직접 삽입하는 대신 Streamlit의 버튼을 사용합니다. -->
    </div>
    """, unsafe_allow_html=True)
    
    # '시작하기' 버튼 구현
    if st.button("시작하기"):
        st.session_state['page'] = 'survey'
        st.experimental_rerun()
        
def display_survey():
    set_page_style()

    question_index = st.session_state.question_index
    if question_index < len(questions):
        question, options, image_url = questions[question_index]
        st.image(image_url, width=700)
        st.markdown(f"### {question}")
        for option in options:
            if st.button(option):
                st.session_state.selected_options.append(option)
                st.session_state.question_index += 1
                if st.session_state.question_index == len(questions):
                    st.session_state.page = 'results'
                st.experimental_rerun()

    else:
        display_results()

# def display_results():
#     set_results_style()
#     st.markdown("## 설문 결과")
#     # 결과 데이터를 바탕으로 결과를 시각화하는 코드
#     # results = pd.Series(st.session_state.selected_options).value_counts()
#     results = pd.Series(st.session_state.selected_options)
#     # 결과 시리즈의 각 항목에 대해 score_dict에서 해당하는 점수를 찾아 리스트에 저장
#     converted_scores = results.map(score_dict).tolist()

#     # 변환된 점수의 총합 계산
#     total_score = sum(converted_scores) 
#     print(total_score)
#     # st.bar_chart(results)

#     if total_score > 1:

        
    
#     if st.button('다시 시작하기'):
#         st.session_state.page = 'cover'
#         st.session_state.question_index = 0
#         st.session_state.selected_options = []
#         st.experimental_rerun()

def display_results():
    set_results_style()
    st.markdown("## 설문 결과")

    results = pd.Series(st.session_state.selected_options)
    converted_scores = results.map(score_dict).tolist()
    total_score = sum(converted_scores)

    # 점수에 따른 결과 이미지 및 메시지 정의
    if total_score >= 10:
        image_url = "https://cdn.metavv.com/prod/uploads/10749482/images/168542440895775.png"
        message = "축하합니다! 당신은 매우 높은 점수를 얻었습니다!"
    elif total_score >= 5:
        image_url = "https://cdn.metavv.com/prod/uploads/10749482/images/168542440895775.png"
        message = "잘 했어요! 당신은 평균 이상의 점수를 얻었습니다."
    else:
        image_url = "https://cdn.metavv.com/prod/uploads/10749482/images/168542440895775.png"
        message = "노력이 필요해요. 더 나은 결과를 위해 다시 시도해보세요."

    # 결과 이미지와 메시지 표시
    st.image(image_url, width=700)
    st.markdown(f"### {message}")

    if st.button('다시 시작하기'):
        st.session_state.page = 'cover'
        st.session_state.question_index = 0
        st.session_state.selected_options = []
        st.experimental_rerun()



def main():
    if st.session_state.page == 'cover':
        display_cover()
    elif st.session_state.page == 'survey':
        display_survey()
    elif st.session_state.page == 'results':
        display_results()

if __name__ == "__main__":
    main()