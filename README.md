# DecisionTreeClassifier


CSV파일 링크
------------
https://www.dropbox.com/s/i8l7jgps1sfehe2/datamining2.csv?dl=0



문제
------------
전체 12,669개(class-1 : 6654개 / class-0 : 6015개)

-조건
1. 300x12669의 데이터를 가진 CSV 파일을 최적의 분기점을 찾아 1또는 0을 정확하게 분류 (300번쨰 열이 0과 1의 데이터를 가짐)
2. Tree는 무조건 2개로 분기
3. depth제한 x, 여러 속성 사용가능



문제 해결
------------
python에서 제공하는 머신러닝 라이브러리인 scikit-learn을 사용

sckit learn에서 제공하는 DecisionTreeClassifier 를 이용하여 분기값을 찾아냄

pydot,GraphViz를 사용 DecisionTree를 시각화

DecisionTreeClassifier에 옵션을 주어 정확도 향상

max_depth – max depth를 상승시킬 시 정확도는 높아지지만 오버피팅 되어 테스트셋을 이용하여 실행할 때 낮은 정확도를 보일 수 있어 max_depth를 7로 설정

random_state – 난수를 0으로 설정

min_samples_split - 리프노드에 있어야하는 최소 샘플 수를 50으로 설정

min_impurity_split – 트리의 분류 여부에 대한 임계값. 임계값을 초과시 노드가 분리


트리 설계도
------------

<img width = "700" src = "https://user-images.githubusercontent.com/62198891/88358046-70452180-cda8-11ea-9d57-1a78c9f3e06b.png">


정확도
------------
<img width = "700" src = "https://user-images.githubusercontent.com/62198891/88358124-b306f980-cda8-11ea-9302-f1197b200c0c.png">

정확도를 Matlab에서 확인해본 결과 87.89%


