# image cutting & merge test
### 개발 환경
- python == 3.8
### requirements
- numpy == 1.24.2
- opencv == 4.7.0
- pandas == 2.0.0
### 디렉토리 구조
```
test   
    ├─assignment  
    │  ├─  cut_image.py  
    │  ├─  merge_image.py  
    │  ├─  testautimation.sh
    │  └──image
    │      ├─  origin.jpeg   
    │      └─  crooped_images  
    │            ├─ cropped_4221923.jpg  
    │            ├─ cropped_4684396.jpg  
    │            ├─ cropped_8259875.jpg  
    │            └─ cropped_9293891.jpg  
    │                
    └─ dev_test  
    │    ├─  merge_img_test.ipynb  
    │    ├─  meta_ai_test_1.ipynb  
    │    └─  stitching_test.ipynb  
    └─  readme.md   
 ```     

- 제출할 과제 파일은 **assingment** 폴더 아래 위치
- 과제진행을 위한 원본 이미지 샘플은 image 경로 아래 origin.jpeg로 위치하며, 다른 이미지를 사용할 경우 외부인자로 파일 경로를 받아 사용할 수 있음
- cropped_image 경로는 분할한 이미지를 저장하는 폴더
- dev_test는 과제를 진행하면서 적용할 수 있는 방법들에 대한 테스트를 진행한 파일을 보관
- testautomation.sh 스크립트 구성 쉘 스크립트 외부 파라미터 입력
    - sh testautomation.sh {columns} {rows} {origin_image_path(optional)}
    - 이미지 경로는 옵셔널하게 입력할 수 있고, 입력하지 않는다면, 테스트 이미지로 사용됨

### 개발 과정
##### 1. cut_imgae.py
- cut_image.py의 경우 과제에서 주어진 내용과 동일하게, 입력된 column과 row에 맞춰 분할을 하고, 각 50%의 확률로 mirroring, flipping, 90 degree rotation을 구현
- 확률값은 random함수를 사용해 난수를 발생시켜, 0.5 이상인 경우 해당 변환이 적용되도록 구현
- 분할된 이미지의 정보를 알 수 없도록 파일명도 난수를 생성하여, 저장하였음

##### 2. merge_imgae.py
- 해당 과제는 구현하지 못함
- 90degree rotation을 처리하기 위해, image의 resolution을 하나의 기준이미지와 동일하게 처리하여 해결
- 과제에서 주어진 정보를 기반으로 Edge Detection을 사용하여, 서로 연결되는 edge를 찾고 지표를 만드는 방법을 구현하지 못함
- Edge Detection의 경우 분할된 이미지를 병합할 경우와, 분할된 이미지의 Edge를 검출한 결과를 각각 병합하여 확인해본 결과,
부적절한 이미지 병합이 발생한 경우 병합된 경계에 직선이 발생하는 특징을 찾아 병합로직을 구현하려 했으나,
이미지의 변환 정보를 알 수 없고, 경계지점의 Edge 총 합의 값을 사용하여 검출하려 했으나, 원본이미지로 복원하기 위해 경우의 수가
분할 영역이 늘어남에 따라 기하급수적으로 증가하였고, 어두운 부분에서의 Edge Detection의 검출률 저하로 연속된 Edge의 특징을 평가할
지표의 기준을 만들 수 없었음
- 추가로 image stitching 기법을 사용하여 병합을 수행하려고 해보았으나, stitching 알고리즘을 사용하기 위해서는 이미지를 분할할시,
특징점을 매칭할 수 있는 공통 부분을 고려하여 분할해야하는데, 주어진 과제에서 분할시 해당 부분을 고려하면 안되는 것으로 생각되어
테스트만 진행하였고, 8가지 변환 케이스에 대한 stitching을 분할 영역에 대해 하나씩 확인하는 과정에 많은 리소스가 할당되어
과제를 해결하는 방안은 아니라고 판단함
