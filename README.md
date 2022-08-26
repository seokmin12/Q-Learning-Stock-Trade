
## Keras를 이용한 가상 주식 매매 인공지능

> 이 인공지능은 유명 딥러닝 유튜버인 Siraj Raval의 영상을 요약하여 정리한 [KerasKorea](https://github.com/KerasKorea/KEKOxTutorial/blob/master/22_Keras%EB%A5%BC%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EC%A3%BC%EC%8B%9D%20%EA%B0%80%EA%B2%A9%20%EC%98%88%EC%B8%A1.md)의 한국어 문서를 바탕으로 일부 수정, 추가하여 제작하였습니다.
### 라이브러리 다운로드

Python 3.8 필요한 라이브러리를 설치하기 위해 `pip install -r requirements.txt`를 실행하세요.


### 활용할 코드와 데이터

원본 코드와 데이터는 [여기](https://github.com/llSourcell/Q-Learning-for-Trading)에서 확인할 수 있습니다. `Python 2.7.`로 쓰여 있습니다.

- `agent.py`: Deep Q Learning `에이전트`가 구현되어 있습니다.
- `envs.py`: 3개의 주식에 대한 거래 환경이 구현되어 있습니다.
- `model.py`: Q 함수로 쓰이는 Multi-layer Perceptron이 구현되어 있습니다.
- `utils.py`: 유용한 함수들이 포함되어 있는 파일입니다.
- `run.py`: 학습/테스트를 할 수 있는 메인 코드입니다.
- `requirement.txt`: 의존성 파일입니다. `pip install -r requirements.txt`로 필요한 라이브러리를 설치할 수 있습니다.
- `data/`: 데이터는 `data` 폴더 내에 있는 3개의 csv 파일을 활용합니다. 각각 IBM, MSFT, QCOM의 주가 데이터로, 2000년 1월 3일부터 2017년 12월 27일까지 5629 거래일의 데이터가 포함되어 있습니다. 이 데이터들은 [Alpha Vantage API](https://www.alphavantage.co/)를 활용해 받았습니다.
- `get_data.py`: 주식 가격을 csv파일로 다운받을 수 있습니다.



### 코드 실행시키는 방법

- **Deep Q `에이전트`를 훈련시키려면**

  `python run.py --mode train` 명령어를 실행합니다. 여러가지 추가 옵션이 있는데, 다음과 같습니다.

  - `-e`, `--episode`: (기본값: 2000) 실행시킬 `에피소드`의 수를 정해줍니다.
  - `-b`, `--batch_size`: (기본값: 32) `배치 사이즈`를 정해줍니다.
  - `-i`, `--inital_invest`: (기본값: 20000) 초기 투자 금액을 정해줍니다.

- **훈련된 모델의 성능을 테스트하려면**

  `python run.py --mode test --weights <trained_model>` 명령어를 실행합니다. `<trained_model>` 는 훈련된 모델의 `weight`가 저장된 경로입니다. 이 명령어를 실행하면 테스트 데이터 포트폴리오의 `에피소드` 당 가치 변화가 저장됩니다.

