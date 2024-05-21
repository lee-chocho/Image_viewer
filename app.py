import streamlit as st
from PIL import Image, ImageEnhance

# 기본 페이지
def main_page():
    st.title("Welcome! Medical Image Viewer")
    st.write("This web app is designed for uploading and editing medical images.")
    st.write("You can upload images and apply various editing functions using the sidebar on the left.")
    st.write("Upload an image and try it out yourself!")

# 이미지 뷰어 기능
def image_viewer():

    # 사이드바에 타이틀 추가
    st.sidebar.header("Image Viewer")

    # 사이드바에 파일 업로드 위젯 추가
    uploaded_files = st.sidebar.file_uploader("Upload image", type=["jpg", "jpeg", "png", "dcm"], accept_multiple_files=True)

    # 선택된 이미지 표시를 위한 인덱스
    if uploaded_files:
        selected_index = st.sidebar.selectbox("Select image", range(len(uploaded_files)), format_func=lambda x: f"image {x + 1}")

        # 파일을 이미지로 읽기
        uploaded_file = uploaded_files[selected_index]
        image = Image.open(uploaded_file)

        # 이미지 조작 기능
        st.sidebar.header("Adjust the image")

        # 명도 조절
        brightness_factor = st.sidebar.slider("Brightness", 0.1, 5.0, 1.0)
        brightness_enhancer = ImageEnhance.Brightness(image)
        brightened_image = brightness_enhancer.enhance(brightness_factor)

        # 대비 조절
        contrast_factor = st.sidebar.slider("Contrast", 0.1, 5.0, 1.0)
        contrast_enhancer = ImageEnhance.Contrast(brightened_image)  # 이전 조작 이미지 사용
        contrasted_image = contrast_enhancer.enhance(contrast_factor)

        # 선명도 조절
        sharpness_factor = st.sidebar.slider("Sharpness", 0.1, 5.0, 1.0)
        sharpness_enhancer = ImageEnhance.Sharpness(contrasted_image)  # 이전 조작 이미지 사용
        sharpened_image = sharpness_enhancer.enhance(sharpness_factor)

        # 회전
        rotation_angle_input = st.sidebar.text_input("Rotation", 0)
        try:
            rotation_angle = float(rotation_angle_input)
            rotated_image = sharpened_image.rotate(rotation_angle)  # 이전 조작 이미지 사용
        except ValueError:
            st.sidebar.warning("Please enter a valid angle.")

        # 이미지 표시
        st.image(rotated_image, caption="Image manipulation result", width=None)

        # 이미지 정보 표시
        st.write(f"size: {rotated_image.size}")
        st.write(f"format: {rotated_image.format}")
    else:
        st.write("Please upload an image on the left sidebar.")

# 메인 함수
def main():
    st.sidebar.title("Sidebar")
    page = st.sidebar.selectbox("Select the page to navigate to.", ["Home", "Image Viewer"])

    if page == "Home":
        main_page()
    elif page == "Image Viewer":
        image_viewer()

if __name__ == "__main__":
    main()