import streamlit as st
import pandas as pd
import numpy as np

def calculate_character_percentages():
    if 'responses_df' in st.session_state:
        # 설문 결과에 따른 캐릭터 유형 점수 계산
        responses = st.session_state['responses_df']
        scores = responses.applymap(lambda x: score_dict.get(x, 0)).sum(axis=1)
        # 각 캐릭터 유형별로 점수 범위를 정의하고, 해당 범위에 따라 결과를 분류
        # 이 예제에서는 단순화를 위해 점수 계산 방식을 직접 구현하지 않았습니다. 실제 적용 시 점수에 따른 캐릭터 분류 로직이 필요합니다.
        # 결과 DataFrame을 생성
        results = pd.DataFrame({'Character': ['트렌드탐험대장', '그린스타일리스트', '모던스타일리스트', '환경우주탐험가'], 'Count': [0, 0, 0, 0]})
        # 여기에 실제 점수에 따라 results DataFrame을 업데이트하는 로직 추가
        # 전체 응답 수
        total_responses = len(responses)
        if total_responses > 0:
            # 비율 계산
            percentages = results['Count'] / total_responses * 100
            results['Percentage'] = percentages
            return results.set_index('Character')['Percentage']
        else:
            return pd.Series()
    else:
        return pd.Series()

def display_intro():
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src=>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("# 옷BTI 설문조사")

    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; align-items: center;">
            <img src="https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihY_0u1jNGWUTviOMpXd070NZpzE16IghexyAXsMxlomGi6L2zpQ-3cjWhPV4Xe55SF1QZ6oSrPYUJFs_xmvHohi81kC=w959-h910" style="width: 33.33%; height: auto; max-height: 24rem;">
            <div style="width: 33.33%; text-align: center;">
                <p> '누군가의 손톱을 먹으면 그 사람의 패션 소비 습관과 스타일을 그대로 따라할 수 있는 능력을 지닌 찍찍이. <br>어느 날 눈을 뜨니 당신의 손톱이 반달 모양으로 패어 있는 것을 발견하는데… <br>과연 찍찍이는 치즈마을에서 어떤 쥐로 자라게 될까?' </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("찍찍이 유형 확인하기", key="start_survey"):
        st.session_state['page'] = 'survey'
        st.rerun()

def set_page_style():
    st.markdown("""
    <style>
    /* 앱 전체 스타일 조정 */
    .stApp {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    /* 버튼 기본 스타일 */
    .stButton>button {
        border: 2px solid rgba(128, 128, 128, 0.5);
        background-color: transparent; /* 버튼 기본 배경색 제거 */
        color: rgb(0, 0, 0); /* 버튼 기본 텍스트 색상 */
        padding: 10px 24px;
        border-radius: 20px;
        font-size: 16px;
        display: block;
        margin: 20px auto;
        width: fit-content;
    }
    /* 버튼 호버 스타일 */
    .stButton>button:hover {
        border: 2px solid rgba(0, 0, 0, 0.1);
        background-color: rgb(255, 215, 0); /* 호버 시 색상 채우기 */
        color: white;
    }
    /* 이미지 스타일 조정 */
    .stImage>img {
        max-width: 50%; /* 이미지 크기 조정, 예: 50%로 줄임 */
        margin-bottom: 20px; /* 이미지와 텍스트 사이 간격 */
    }
    /* 설문 질문 글꼴 크기 확대 */
    .markdown-text-container, .stMarkdown {
        text-align: center !important;
        font-size: 20px !important; /* 글꼴 크기 조정 */
    }
    </style>
    """, unsafe_allow_html=True)

# 캐릭터 카운트를 초기화하는 코드는 앱의 초기 설정 부분에 배치
if 'character_counts' not in st.session_state:
    st.session_state.character_counts = {'트렌드탐험대장': 0, '그린스타일리스트': 0, '모던스타일리스트': 0, '환경우주탐험가': 0}



# 페이지 설정 및 CSS 스타일 적용
st.set_page_config(page_title="옷BTI 테스트", layout="wide")
set_page_style()  # 페이지 스타일 설정을 여기에 호출하여 모든 페이지에 적용

questions = [
    ("1. ‘오늘부터 단 7일! 고객님만을 위한 특별 할인 쿠폰!’ 카톡이 울렸다. 이때 나의선택은?", 
     ["옷을 살 생각은 없었지만 세일을 한다고 하니 일단 구경한다.", 
      "딱히 옷을 사려고 생각하지 않았으니 무시한다."], 
      "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihY8Tmt5I7J642-aUUYWiqdqtAngOn7E8uurcvMG33Y984xM2-xuZqijWJS3ihPIM7z1GVZQP_IukRq44awsWdzc6BoU=w959-h910"),
    ("2. 앗! 쿠폰이 오늘 사라져요! 고객님이 보유하신 쿠폰이 오늘 만료될 예정입니다.", 
     ["엇!! 내가 호옥시나 필요한 옷이 있을 수도 있으니 12시가 되기 전까지 시간될 때마다 웹서핑을 계속한다.", 
      "이런 타임 어택으로 옷을 사면 실패하거나 충동 구매할 확률이 높으니 다음 기회에!"], 
      "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihYWI5bq0wMjDC84Z5qygX6pq0pkOC_XKyNG8tj_nSRsfHNhveQYCu1tWPXNE834r1jwTgRa7kvSfU3skPHfwWEJyiU3=w959-h910"),
    ("3. 새학기를 맞아 대청소를 결심하고 옷장 문을 열었더니", 
     ["오래 입지 않아 있는 줄도 몰랐던 옷들이 한 무더기로 발견된다.", 
      "매년 옷장 정리를 했기 때문에 어떤 옷들이 있는지 잘 알고 있다."], 
      'https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihaQA9xKJRmUQSG17SkJ2gkwVcdvzpBqWgkKVj3T-LR1q7gTIz5W7KYhn1DCOMnMCvqWW6y0DFfKQfmNHE9YMeiAYN1EKg=w959-h910'),
    ("4. 둘 중 하나를 구매해야 한다면?", 
     ["친환경 소재와 공정을 사용해 만든 코트", 
      "최신 트렌드를 반영해 만든 올해의 SS 상품"], 
     "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihYD6vuDcZ4DuMOxzoIET1MA8yNEazydXUf6xCDyqlwd9glwBZ_vbWYYMsi7D1JtdJd3cbeK5jGlHRmBmGZ9ym9GQ0tKMQ=w959-h910"),
    ("5. 오늘은 개강 첫 주! 아쉽게도 이번 학기는 공강이 없는데,,,", 
     ["적어도 일주일동안 겹치지 않고 입을 정도의 옷들은 있어야지!! 바로 쇼핑을 시작한다.", 
      "에이! 내 옷을 누가 알아본다고!! 적당히 돌려 입는다."], 
     "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihYBEwJGAEaxY7gQHxh5Ie1JAsf5xMwJ01TCiytTKTKQepUFoq_ydQ2FmLel9lnr2wldyR-vwB0adooLJWhzDqOEiAr6Tg=w959-h910"),
    ("6. 옷장정리를 해서 안 입는 옷을 박스에 담았다. 이때 나의 선택은?", 
     ["에이… 언젠간 입겠지. 버리긴 아까우니 입을 일이 있을 때까지 놔둔다.", 
      "난 안 입지만 괜찮은 옷들인데… 헌옷 기부처를 알아본다.",
      "이번 기회에 리폼을 한 번 해볼까? 유튜브에 긴 청바지 리폼 방법을 찾아본다."], 
     "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihZB3z62F5vZn6GYlDzICIZ3CR-mJyl6wREpLOJDt69i95veOyiq0p80rA0CEvNm_KRJyqcaYzJerM3ZC4t42atTLG0aAg=w959-h910"),
     ("7. 우리집 앞에 옷 가게가 생긴다면 내가 더 애용할 곳은?", 
     ["상태가 좋은 구제 옷들을 이용해 다양한 코디를 선보이는 구제샵", 
      "값싼 소재의 옷을 이용해 가성비 좋게 옷을 구매할 수 있는 가게"], 
     "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihbaEu3gUdtSwkRVuNEl5vNBDQnQkAt5OS9CJLcdcJA9efmieyJzDzyDUjtEVLdVV-BOO_vM8Rii_jamuS0_0EehaU7jWQ=w959-h910")
]

# 앱의 초기 설정 부분에서 응답 DataFrame을 초기화합니다.
if 'responses_df' not in st.session_state:
    columns = [f"Question {i+1}" for i in range(len(questions))]
    st.session_state.responses_df = pd.DataFrame(columns=columns)

score_dict = {
    #1
    "옷을 살 생각은 없었지만 세일을 한다고 하니 일단 구경한다." : 5, 
    "딱히 옷을 사려고 생각하지 않았으니 무시한다." : 0,
    #2
    "엇!! 내가 호옥시나 필요한 옷이 있을 수도 있으니 12시가 되기 전까지 시간될 때마다 웹서핑을 계속한다." : 5, 
    "이런 타임 어택으로 옷을 사면 실패하거나 충동 구매할 확률이 높으니 다음 기회에!" : 0,
    #3
    "오래 입지 않아 있는 줄도 몰랐던 옷들이 한 무더기로 발견된다." : 5, 
    "매년 옷장 정리를 했기 때문에 어떤 옷들이 있는지 잘 알고 있다." : 0,
    #4
    "친환경 소재와 공정을 사용해 만든 코트" : 0, 
    "최신 트렌드를 반영해 만든 올해의 SS 상품" : 5,
    #5
    "적어도 일주일동안 겹치지 않고 입을 정도의 옷들은 있어야지!! 바로 쇼핑을 시작한다." : 5, 
    "에이! 내 옷을 누가 알아본다고!! 적당히 돌려 입는다." : 0,
    #6
    "에이… 언젠간 입겠지. 버리긴 아까우니 입을 일이 있을 때까지 놔둔다." : 0, 
    "난 안 입지만 괜찮은 옷들인데… 헌옷 기부처를 알아본다." : 5,
    "이번 기회에 리폼을 한 번 해볼까? 유튜브에 긴 청바지 리폼 방법을 찾아본다." : 5,
    #7
    "상태가 좋은 구제 옷들을 이용해 다양한 코디를 선보이는 구제샵" : 0, 
    "값싼 소재의 옷을 이용해 가성비 좋게 옷을 구매할 수 있는 가게" : 5
    }

# Find the maximum number of options in any question
max_options = max(len(options) for _, options, _ in questions)

# Initialize or update the response tracker
if 'response_tracker' not in st.session_state:
    st.session_state['response_tracker'] = pd.DataFrame(0, 
                                                        index=np.arange(len(questions)), 
                                                        columns=[f"Option {i+1}" for i in range(max_options)])
    st.session_state['page'] = 'cover'  # 현재 cover 페이지에 있다고 설정
    st.session_state['question_index'] = 0  # 첫 질문부터 시작
    st.session_state['selected_options'] = []  # 아직 옵션 선택 부분을 빈칸으로


def display_cover():
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="https://cdn.metavv.com/prod/uploads/10749482/images/168542440895775.png" style="width: 33.33%; height: auto; max-height: 24rem;">
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("## 옷BTI 설문조사")
    
    if st.button("Start", key="start"):
        st.session_state['page'] = 'intro'
        st.rerun()

    total_responses = sum(st.session_state.character_counts.values())
    col1, col2, col3, col4 = st.columns(4)

    # 캐릭터 순서와 이미지 URL을 업데이트
    images = [
        "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihY8qdARdLOtkqoTRkqVq3jKVrgqRNnha0AlYUQVuBMBJ5jcDO6hhdBmVWf6cgI1wCp1P9GaRUfJwGh8C7P5silzW8KZ=w959-h910",  # 트렌드탐험대장
        "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihapAmUipxeC3KwTNk33jRKo_HlwB0Fk2_lsqwrCQblBaIepCi2FeK703h1nU9yPib8-vZBRnJw5tQWCjxUOvcjFYlFRTQ=w959-h910",  # 모던스타일리스트
        "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihYyCLJBOT80T0QdzwNNiKsPds_uzRUFIm5LBY1umuzATgkIUbVV5IsRGS3AUrFEmoUNmu6oS8jij-RcL0KHkd2luF3Z=w959-h910",  # 그린스타일리스트
        "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihaWbM9u0o-6dTWCnk05EKdN4tyQ4l8CG-BIGzu96MUh_RtMApucw9aHRFwidUuHQ3BipqXAeT5vxfyy9AoUXqblYp1Nmg=w959-h910"   # 환경우주탐험가
    ]

    headers = ["트렌드탐험대장", "모던스타일리스트", "그린스타일리스트", "환경우주탐험가"]

    for i, col in enumerate([col1, col2, col3, col4]):
        with col:
            st.markdown(f"### {headers[i]}")
            percentage = (st.session_state.character_counts[headers[i]] / total_responses * 100) if total_responses > 0 else 0
            st.write(f"{percentage:.2f}%")
            st.markdown(
                f"""
                <div style="display: flex; justify-content: center;">
                    <img src="{images[i]}" style="width: 100%; height: auto;">
                </div>
                """,
                unsafe_allow_html=True,
            )

def display_survey():
    question_index = st.session_state.question_index
    if question_index < len(questions):
        question, options, image_url_survey = questions[question_index]

        st.markdown(f"## {question}")

        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <img src={image_url_survey} style="width: 33.33%; height: auto; max-height: 24rem;">
            </div>
            """,
            unsafe_allow_html=True,
        )

        for option in options:
            if st.button(option, key=f"{question_index}_{option}"):
                st.session_state.selected_options.append(option)
                st.session_state.question_index += 1
                if st.session_state.question_index == len(questions):
                    st.session_state.page = 'results'
                st.rerun()




def display_results():
    st.markdown("## 설문 결과")

    selected_options = st.session_state.selected_options
    new_row = {f"Question {i+1}": option for i, option in enumerate(selected_options)}
    new_row_df = pd.DataFrame([new_row]) # new_row 딕셔너리를 DataFrame으로 변환
    st.session_state.responses_df = pd.concat([st.session_state.responses_df, new_row_df], ignore_index=True)


    st.session_state.responses_df.to_csv('survey_responses.csv', index=False)


    # 사용자의 선택에 대한 점수를 계산합니다.
    results = pd.Series(st.session_state.selected_options)
    converted_scores = results.map(score_dict).tolist()
    total_score = sum(converted_scores)



    # 총점수에 따라 결과 이미지와 메시지, 그리고 이미지 설명을 결정합니다.
    if total_score >= 30:
        image_url = "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihY8qdARdLOtkqoTRkqVq3jKVrgqRNnha0AlYUQVuBMBJ5jcDO6hhdBmVWf6cgI1wCp1P9GaRUfJwGh8C7P5silzW8KZ=w959-h910"
        message = "트렌드탐험대장"
        description = """
            ‘당신은 ‘트렌드 탐험가’입니다.
            트렌드의 바다를 탐험하며 길을 이끌고 있어요! 트렌드를 따라잡는 데 능숙하며 자기 관리를 즐깁니다.\n
            친환경 옷보다 새로운 트렌드와 인기 패션을 발견하는 것에 더 마음이 반응합니다.\n
            새로운 패션을 통해 나의 취향을 뽐내는 것에 자부심을 느낍니다. 하지만! 과도한 의류 소비로 인한 환경 문제와 비용에 대한 관심이 부족해 보입니다.\n
            그러나! 자신을 너무나도 아끼는 사람이기 때문에, 주변을 조금만 둘러보면 패션과 환경을 모두 아우르는 트렌드 기부 천사가 될 수 있어요.\n
            트렌드 탐험가로서! ‘더 알아보기’를 통해 입지 않는 옷들을 조금씩 기부하는 건 어떨까요? \n
            수정해서 오래 입을 수 있도록 다양한 의상을 시도해 보는 것이 더 재미있을 거예요!\n
            ‘지속 가능한 의류 소비를 추구하는 새로운 트렌드를 탐색하세요!’
            """
        st.session_state.character_counts[message] += 1 
    elif total_score >= 20:
        image_url = "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihapAmUipxeC3KwTNk33jRKo_HlwB0Fk2_lsqwrCQblBaIepCi2FeK703h1nU9yPib8-vZBRnJw5tQWCjxUOvcjFYlFRTQ=w959-h910"
        message = "모던스타일리스트"
        description = """
            당신은, ‘모던 스타일리스트’입니다. \n
            트렌드를 따라가는 당신! 당신은 트렌드를 잘 찾고 트렌드에 맞게 코디하는 걸 즐기는 편이에요. \n
            저렴한 가격이나 품질보다는 요즘 유행하는 패션을 발견하는 것에 더 심장이 반응하기도 한답니다. 그렇다고 비싼 옷을 쉽게 사진 않아요. \n
            적당한 가격의 트렌디한 패션으로 자신을 가꾸는 것에 자부심을 느껴요. 다만, 환경 문제에는 관심이 부족해 보입니다. \n
            But! 그만큼이나 자신에 대해 관심이 많은 사람이기 때문에, 조금만 주위를 둘러보면 패션과 환경 다 아우를 수 있겠군요. \n
            모던 스타일리스트로서! ‘더 알아보기’를 통해 패스트패션이라는 환경문제에 대해 한번 알아보면 어떨까요? \n
            지속가능한 옷 소비를 추구하는, 새로운 트렌드를 탐험해봐요!
            """
        st.session_state.character_counts[message] += 1
    elif total_score >= 10:
        image_url = "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihYyCLJBOT80T0QdzwNNiKsPds_uzRUFIm5LBY1umuzATgkIUbVV5IsRGS3AUrFEmoUNmu6oS8jij-RcL0KHkd2luF3Z=w959-h910"
        message = "그린스타일리스트"
        description = """
            당신은, ‘그린 스타일리스트’입니다.\n
            환경을 생각하는 당신! 당신은 지속가능한 소비를 추구하고 환경문제를 잘 이해하는 편이에요.\n
            유행에 따라가는 것보다는 자신만의 스타일로 옷을 코디하는 것에 더 심장이 반응하기도 한답니다.\n
            필요한 옷을 합리적인 가격에 구매하고 오래 입는 것에 더 자부심을 느껴요.\n
            But! 혹시 패스트 패션이라는 환경문제의 심각성에 대해 잘 모르고 계시진 않았나요?\n
            조금만 더 노력한다면, 다양한 친환경 어플과 업체를 통해 더 합리적이고 지속가능한 옷 소비를 즐길 수 있겠군요.\n
            그린 스타일리스트로서! ‘더 알아보기’를 통해 패스트패션이라는 환경문제에 대해 알아보면 어떨까요? \n
            친환경적인 옷 소비를 추구하는, 새로운 트렌드를 탐험해봐요!
            """ 
        st.session_state.character_counts[message] += 1
    else:
        image_url = "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihaWbM9u0o-6dTWCnk05EKdN4tyQ4l8CG-BIGzu96MUh_RtMApucw9aHRFwidUuHQ3BipqXAeT5vxfyy9AoUXqblYp1Nmg=w959-h910"
        message = "환경우주탐험가"
        description = """
            당신은, ‘환경 우주탐험가’입니다. \n
            지구라는 바다를 탐험하며 앞장서 나가는 당신! \n
            당신은 친환경적인 소비를 추구하고 환경문제의 심각성을 잘 이해하는 편이에요.\n
            유행에 따라가는 것보다는 환경을 위한 행동을 하는 것에 더 심장이 반응하기도 한답니다.\n
            옷을 수선하여 오래 입고 친환경적인 옷 소비를 하는 것에 더 자부심을 느껴요. \n
            But! 혹시 주변 사람들이 패스트패션이라는 환경문제의 심각성에 대해 잘 모르고 있진 않나요?\n
            환경 우주탐험가로서! ‘더 알아보기’를 통해 패스트패션 문제를 주변 사람들에게 공유해보면 어떨까요? \n
            주변 사람들과 함께 친환경적인 옷 소비를 추구하는, 새로운 트렌드를 탐험해봐요!
            """
        st.session_state.character_counts[message] += 1

    description_html = description.replace("\n", "<br>")

    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; align-items: center;">
            <img src="{image_url}" style="width: 33.33%; height: auto; max-height: 24rem;">
            <div style="width: 33.33%; text-align: center;">
                <h2>{message}</h2>
                <p>{description_html}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # '다시 시작하기' 버튼을 제공하여 사용자가 설문조사를 재시작할 수 있도록 합니다.
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button('다시 시작하기'):
            st.session_state.page = 'cover'
            st.session_state.question_index = 0
            st.session_state.selected_options = []
            st.rerun()

def main():
    if st.session_state.page == 'cover':
        display_cover()
    elif st.session_state.page == 'intro': # 설명 페이지 추가
        display_intro()
    elif st.session_state.page == 'survey':
        display_survey()
    elif st.session_state.page == 'results':
        display_results()

if __name__ == "__main__":
    main()