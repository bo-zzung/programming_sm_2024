import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import random

st.title("Vitamin Schedule💊")

# Tabs
tab1, tab2, tab3 = st.tabs(["Home❤️", "💡 Info ", "📝 Schedule"])
data = np.random.randn(10, 1)

with tab1:
    greetings = [
        "You've got this! Stay strong, stay focused, and make today your masterpiece",
        "You're unstoppable! Embrace today's challenges, overcome obstacles, and thrive",
        "Believe in yourself! With determination and positivity, you can conquer anything",
        "Embrace the day! Your strength and resilience will lead you to success!",
        "You're amazing! Let your positivity shine and make each moment count!",
        "Be fearless! Face challenges with courage, and watch yourself soar!",
        "Stay bold! With passion and perseverance, you'll achieve greatness today!"
    ]
    
    image_file = [
        "happy1.jpeg",
        "happy2.jpg",
        "happy3.jpg"
    ]

    # Random selection
    random_greeting = random.choice(greetings)
    random_image_file = random.choice(image_file)
    st.title(f"""Hey there, busy bee!
    This one's for all you modern-day hustlers out there.
    {random_greeting}
    Let's power up with some vitamins and conquer the day together""")
    with open(random_image_file, "rb") as f:
        image = f.read()
    st.image(image, use_column_width=True)

with tab2:
    vitamin_details = {
        "글루타치온": "글루타치온은 항산화 작용을 하는 물질로, 간 해독을 돕고 면역력을 증진시키는 데 도움을 줍니다.",
        "마그네슘": "마그네슘은 근육 이완과 신경 전달, 에너지 생성에 중요한 역할을 합니다.",
        "밀크씨슬": "밀크씨슬은 간 건강을 지원하며, 간 세포를 보호하고 재생을 촉진하는 데 도움을 줍니다.",
        "비타민 A": "비타민 A는 시력 유지와 면역 기능에 중요하며, 피부 건강을 촉진합니다.",
        "비타민 B": "비타민 B군은 에너지 대사와 신경 기능에 중요한 역할을 합니다.",
        "비타민 C": "비타민 C는 항산화 작용을 하며, 면역력 증진과 피부 건강에 도움을 줍니다.",
        "비타민 D": "비타민 D는 칼슘 흡수를 도와 뼈 건강을 유지하는 데 중요합니다.",
        "아르기닌": "아르기닌은 혈액 순환을 개선하고, 성장 호르몬 분비를 촉진합니다.",
        "유산균": "유산균은 장 건강을 유지하고 소화 기능을 개선하는 데 도움을 줍니다.",
        "이외트피": "이외트피는 전반적인 건강 증진에 도움을 줍니다.",
        "오메가-3": "오메가-3는 심혈관 건강을 지원하고 염증을 줄이는 데 도움을 줍니다.",
        "코엔자임 Q10": "코엔자임 Q10은 에너지 생산을 도와 피로를 줄이고, 심장 건강을 지원합니다.",
        "칼슘": "칼슘은 뼈와 치아 건강을 유지하는 데 중요하며, 근육 기능을 지원합니다.",
        "철분": "철분은 혈액 생성과 산소 운반에 중요한 역할을 합니다.",
        "홍삼": "홍삼은 면역력 증진과 피로 회복, 혈액 순환 개선에 도움을 줍니다.",
        "루테인": "루테인은 눈 건강을 유지하고 황반 변성을 예방하는 데 도움을 줍니다.",
        "망간": "망간은 뼈 건강과 에너지 대사에 중요합니다.",
        "아연": "아연은 면역 기능과 상처 치유, 단백질 합성에 중요한 역할을 합니다."
    }
    
    vitamin_warnings = {
        "글루타치온": "주의사항: 임산부나 수유 중인 여성은 의사와 상의하세요.\n부작용: 위장 장애가 발생할 수 있습니다.",
        "마그네슘": "주의사항: 신장 문제가 있는 경우 피하세요.\n부작용: 설사를 유발할 수 있습니다.",
        "밀크씨슬": "주의사항: 알레르기 반응이 있을 수 있습니다.\n부작용: 위장 장애가 발생할 수 있습니다.",
        "비타민 A": "주의사항: 과다 복용 시 독성이 있을 수 있습니다.\n부작용: 두통, 어지러움이 발생할 수 있습니다.",
        "비타민 B": "주의사항: 복용 시 과량을 피하세요.\n부작용: 간헐적인 위장 장애가 발생할 수 있습니다.",
        "비타민 C": "주의사항: 신장 결석의 위험이 있을 수 있습니다.\n부작용: 설사를 유발할 수 있습니다.",
        "비타민 D": "주의사항: 과다 복용 시 고칼슘혈증이 발생할 수 있습니다.\n부작용: 메스꺼움, 구토가 발생할 수 있습니다.",
        "아르기닌": "주의사항: 심장 질환이 있는 경우 피하세요.\n부작용: 위장 장애, 두통이 발생할 수 있습니다.",
        "유산균": "주의사항: 면역 억제제를 복용 중인 경우 피하세요.\n부작용: 복부 팽만감이 발생할 수 있습니다.",
        "이외트피": "주의사항: 특정 질환이 있는 경우 의사와 상의하세요.\n부작용: 위장 장애가 발생할 수 있습니다.",
        "오메가-3": "주의사항: 혈액 희석제를 복용 중인 경우 피하세요.\n부작용: 메스꺼움, 설사가 발생할 수 있습니다.",
        "코엔자임 Q10": "주의사항: 혈압 강하제를 복용 중인 경우 피하세요.\n부작용: 복부 통증, 설사가 발생할 수 있습니다.",
        "칼슘": "주의사항: 신장 결석의 위험이 있을 수 있습니다.\n부작용: 변비가 발생할 수 있습니다.",
        "철분": "주의사항: 과다 복용 시 중독이 발생할 수 있습니다.\n부작용: 위장 장애, 변비가 발생할 수 있습니다.",
        "홍삼": "주의사항: 고혈압이 있는 경우 피하세요.\n부작용: 불면증, 두통이 발생할 수 있습니다.",
        "루테인": "주의사항: 과량 복용 시 부작용이 있을 수 있습니다.\n부작용: 소화 장애가 발생할 수 있습니다.",
        "망간": "주의사항: 과량 복용 시 독성이 있을 수 있습니다.\n부작용: 신경 장애가 발생할 수 있습니다.",
        "아연": "주의사항: 과다 복용 시 면역 기능 저하가 발생할 수 있습니다.\n부작용: 위장 장애, 메스꺼움이 발생할 수 있습니다."
    }

    st.divider()
    st.title("Vitamin's Info")
    st.caption("알고싶은 정보의 영양제를 클릭해보세요👆")
    st.divider()

    info_text = st.empty()
    warning_text = st.empty()

    cols = st.columns(3)  # 3 columns

    for i, (vitamin, detail) in enumerate(vitamin_details.items()):
        col = cols[i % 3]
        if col.button(vitamin):
            info_text.text_area("영양제 정보", value=detail, height=150)
            warning_text.warning(vitamin_warnings[vitamin], icon="⚠️")

with tab3:
    vitamin_info = pd.DataFrame({
        "영양제": [
            "글루타치온", "마그네슘", "밀크씨슬", "비타민 A", "비타민 B", "비타민 C",
            "비타민 D", "아르기닌", "유산균", "이외트피", "오메가-3", "코엔자임 Q10",
            "칼슘", "철분", "홍삼", "루테인", "망간", "아연"
        ],
        "아침": ["1(식전)", "x", "1(식후)", "x", "1(식후)", "1(식후)", "1(식후)", "1(식후)", "1(식전)", "1(식후)", "x", "1(식후)", "x", "1(식전)", "1(식후)", "1(식후)", "1(식후)", "x"],
        "점심": ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
        "저녁": ["x", "1(식후)", "1(식후)", "1(식후)", "x", "1(식후)", "x", "1(식후)", "x", "x", "1(식후)", "x", "1(식후)", "x", "x", "x", "x", "1(식후)"]
    })

    selected_vitamins = st.sidebar.multiselect(
        "복용 중인 영양제를 선택하세요",
        vitamin_info["영양제"].tolist()
    )

    cols = st.columns([1, 1])  # Two equal columns for Create Schedule and Download buttons

    with cols[0]:
        create_button = st.button("Create Schedule")

    if create_button:
        if selected_vitamins:
            schedule = vitamin_info[vitamin_info["영양제"].isin(selected_vitamins)].set_index("영양제")

            st.write("오늘 하루의 비타민 스케줄:")
            st.dataframe(schedule, use_container_width=True)

            # Create textual summary
            morning_vitamins = schedule[schedule['아침'] != 'x']
            lunch_vitamins = schedule[schedule['점심'] != 'x']
            evening_vitamins = schedule[schedule['저녁'] != 'x']

            def create_summary(vitamin_series):
                return ", ".join([f"{vitamin} ({dose})" for vitamin, dose in vitamin_series.items()])

            st.header("**Morning🌅**")
            st.write(f": {create_summary(morning_vitamins['아침'])}")

            st.header("**Lunch🍚**")
            st.write(f": {create_summary(lunch_vitamins['점심'])}")

            st.header("**Evening🌉**")
            st.write(f": {create_summary(evening_vitamins['저녁'])}")

            # Display the Download button in the second column
            with cols[1]:
                csv = schedule.to_csv(index=True).encode('utf-8')
                st.download_button(
                    label="Download",
                    data=csv,
                    file_name="schedule.csv",
                    mime="text/csv"
                )
            
        else:
            st.write("영양제를 선택해주세요.")
