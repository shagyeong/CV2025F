import numpy as np
import cv2

def user_shear(src):
    r=src.shape[:2][0]             # row size
    c=src.shape[:2][1]             # column size

    # shear factor 선택
    if np.random.choice([0,1]): # 수평 밀림
        sf_x=np.random.uniform(-0.2,0.2)
        sf_y=0
    else:                       # 수직 밀림
        sf_x=0
        sf_y=np.random.uniform(-0.2,0.2)

    # 어파인 변환 행렬
    M=np.float32([
        [1, sf_x, 0],
        [sf_y, 1, 0]
    ])

    # 잘림 방지를 위한 영상 크기 확산
    c_upscale=int(c*1.5)
    r_upscale=int(r*1.5)

    # 어파인 변환 적용
    # borderMode=cv2.BORDER_CONSTANT를 사용하여 빈 공간을 0(검은색)으로 채움
    dst=cv2.warpAffine(
        src,
        M,
        (c_upscale,r_upscale),
        borderMode=cv2.BORDER_CONSTANT, # 사용자 지정 값으로 빈 공간 채움
        borderValue=(0,0,0)             # 검정색으로 채움
    )

    # 원본 이미지 크기로 다운스케일
    dst = cv2.resize(dst, (c, r), interpolation=cv2.INTER_AREA)

    return dst