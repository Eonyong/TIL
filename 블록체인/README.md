## 블록체인(Block-chain)

---

## 목차





## 블록체인이란?

---

* 일종의 "데이터 분산 처리 기술"
* 네트워크에 참여하는 모든 사용자가 모든 거래 내역 등의 데이터를 분산, 저장하는 기술을 지칭
* 개개인 간 거래(P2P)가 발생할 경우, 네트워크에 참가하는 모든 사용자에게 거래가 공유되고 해당 거래가 모두 일치하는지 대조를 진행
* 위 경험 때문에 __"공공 거래장부"__ 혹은 __"분산 거래장부"__로 불림



## 특징

---

* 기존 거래 방식은 은행이 모든 거래 내역을 가지고 있고 은행을 거쳐서만 거래가 가능한 방식이라면, 블록체인방식은 거래 내역을 모든 네트워크 사용자가 1/N만큼 가지고 있고 이를 연결하여 진위 여부를 확인한다는 차이가 있음

* 분산저장

  > 기존 거래 방식에서는 은행의 중앙 서버가 공격 당하면 고객의 거래 데이터가 손실을 입지만, 블록체인의 경우, 모든 네트워크 사용자에게 공격을 해야 하므로 위 변조가 어려움 -> ~~사실상 해킹이 어렵다고 말하고 있다.~~

* 중앙 관리자가 필요 없음

* 높은 신뢰성과 보안성



## 블록과 체인 구현

---

* 블록

* > 다수의 거래 정보의 묶음
  >
  > 블록 헤더는 __version__, __previousblockhash__, __merklehash__, __time__, __bits__, __nonce__ 이렇게 6개의 정보로 구성
  >
  > 거래 정보는 입출금과 관련한 여러 정보를 담고 있음
  >
  > 기타 정보는 블록 내에 있는 정보 중에서 블록 헤더와 거래 정보에 해당하지 안흔 ㄴ정보를 말하며, 블록 해쉬 계산에 사용되니 않음

* 체인 - 연결고리

* 이를 코드로 구현한다면, 구조체 값에 링크드 리스트를 엮은 모습과 흡사. 다만, 포인터가 아닌 해시로 참조해야하므로 해시함수에 대한 이해가 필요함



## 블록해더

---

* __version__: SW / protocol 버전
* __previousblockhash__: 블록 체인에서 바로 앞에 위치하는 블록의 블록 해쉬
* __merklehash__: 개별 거래 정보의 거래 해쉬를 2진 트리 형태로 구설할 때, 트리 루트에 우치하는 해시값
* __time__: 블록이 생성된 시간
* __bits__:난이도 조절용 수치
* __nonce__:최초 0에서 시작하여 조건을 만족하는 해시값을 찾아낼 때까지 1씩 증가하는 계산 횟수



## 해시함수의 특징

---

* 해시함수란 임의 길이의 데이터를 고정된 길이의 데이터로 매핑하는 함수
* 어떠한 값을 입력하면 비슷한 길이의 난수가 출력
* 입력값이 하나만 바껴도 완전히 다른 난수가 출력
* 츨력으로 입력을 예측할 수 없다
* 그렇지만 입력이 같으면 출력은 항상 같다



## 블록구현

---

* 블록은 구조체로 표현될 수 있음
* 가장 단순한 모델 = 이전 블록의 해시값을 기억할 변수 + 현재 블록에서 간직해야 할 데이터



## 체인구현

---

* 블록 생성 후 직전에 만든 블록과의 관계를 맺어줍니다. 이전의 블록 해시값을 그 다음 블록이 기억을 해주고 이런 과정을 반복적으로 해주는 관계 > __"블록체인"__이라 부릅니다
* 단 하나의 예외의 경우는 최초 블록을 생성할 때이다. 이는 이전의 블록이 존재하지 않기 때문에 해시값이 없거나 무의미한 랜덤 값을 넣어 줍니다. 이러한 최초의 블록을 __Genesis블록__이라고 함



## 작업증명

---

* 목표값 이하의 해시를 찾는 과정을 무수히 반복하여 해당 작업에 참여했음을 증명하는 방식의 __합의 알고리즘__ > 이는 어떤 트랜잭션이 발생했을 경우 해당 트랜잭션이 유효한 트랜잭션인지에 대한 합의 방법 및 새로운 블록의 진위 검증을 수행
* 3개의 블록이 있는 블록체인이 있다고 가정해보겠습니다.

> 2번째 블록의 해시값이 있고 이를 3번째 블록에서 기억을 하고 있습니다.
>
> 그러나 2번 블록에서 누군가 수정을 한다면, 2번째 이후의 블록에서 기억하고 있는 해시값을 수정 해줘야 합니다. 그렇게 되면 3번째 블록의 해시값 자체도 수정이 이루어지게 되는데 이를 손수 수정해서 이뤄져야 합니다.
>
> 하지만, 3개 정도면 컴퓨터가 금방 수정할 수 있지만 블록의 수가 계속 증가하고 제약 조건도 증가한다면 수정하는 시간이 점점 증가할 것입니다.

* __[Nonce](#http://wiki.hash.kr/index.php/%EB%85%BC%EC%8A%A4_(%EC%9E%84%EC%8B%9C%EA%B0%92))__(임시값)

  > 보통 사용하는 방법으로는 해시값의 가장 앞이 "0"으로 시작하는 해시값을 구하도록 유도하는 것입니다. 이렇게하면 랜덤 값을 입력 했을 때, 가장 앞이 "0"으로 보장 되지 않기 때문에 이를 찾기 위해 이전보다 시간이 더 걸릴 것입니다. 만약 "00"으로 설정한다면 더 많은 시간이 소요될 것입니다. 이러한 조건을 주는 값 Nonce라 부름
  >
  > __블록 헤더에서 유일하게 값이 확정되지 않아 수정이 가능한 항목__

* __채굴__ <작업 증명과 보상을 합친 개념??>

  > 쉽게 말하면 암호화폐의 거래내역을 기록한 블록을 생성하고 그 대가로 암호화폐를 얻는 행위
  >
  > 임의의 Nonce 값을 대입하여 얻은 결과 값이 제사된 타겟보다 작은 결과 값이 나올때까지 무한하게 작업이 실행
  >
  > 이러한 수학 문제 풀이 과정을 1초에 몇번이나 수행할 수 있는지에 대한 수치 정보 > __해시파워__

* __작업 난이도__

  > 논스 값 계산의 어려운 정도
  >
  > 블록 헤더 정보에서 __bits__라는 값으로 조절됨
  >
  > 난이도는 2160개의 블록이 생성되는데 소요되는 시간이 평균 시간인 21600분보다 적게 걸리면 난이도가 올라가고 오래 걸리면 난이도가 낮아지는 방식

* __보상__

  > 새로 발행되는 비트코인과 해당 블록에 포함되는 거래의 거래 수수료의 합
  >
  > 비트코인에서 비트코인의 새로운 발행은 채굴자가 블록을 처음 구성할 때 채굴자의 지갑으로 일정량의 비트코인이 입금되는 거래를 그 블록의 첫 거래로 추가하는 방식으로 이루어진다. 새로 발행되는 비트코인은 최초에 05BTC에서 시작하여 블록 체인에 21만개의 블록이 추가될 때마다 절반으로 줄어듦
  >
  > 거래 수수료의 경우 거래 당사자간 자율적으로 정할 수 있고, 거래가 블록에 추가되는 우선순위를 결정하는데 거래 수수료가 입력 값으로 사용되기도 함



[참고 코드]: https://rudalson.tistory.com/entry/%EA%B0%84%EB%8B%A8%ED%95%9C-%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8%EC%9D%84-%EA%B5%AC%ED%98%84%ED%95%B4%EB%B3%B4%EB%A9%B0-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0

![image-20211223165626051](%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8(Block-chain)%20%EB%B0%8F%20%ED%95%B4%EC%8B%9C%EC%9D%98%20%EC%9D%B4%ED%95%B4.assets/image-20211223165626051.png)