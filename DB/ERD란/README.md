## DB 설계, ERD 작성 실습

---

## 목차

* [ER 데이터 모델](#er-데이터-모델)
* [엔티티](#엔티티)
* [어트리뷰트](#어트리뷰트)
* [관계](#관계)
* [엔티티 타입](#엔티티-타입)





## ER 데이터 모델

---

* 개념적 데이터 모델
* 엔티티(Entity), 어트리뷰트(Attribute), 관계(Relationship)를 이용해서 개념적으로 표현한 기법



## 엔티티

---

* 어트리뷰트를 담는 상자
* 모델의 관리 대상
* 사람, 물건, 장소 등이나 개념을 엔티티로 선택
* 시스템 구축 단계까지 진행되면 파일이나 데이터베이스의 테이블로 구현
* ER 다이어그램에서는 사각형으로 표현
* ER 모델에서 가장 기본이 되며, 고유하게 식별되어야 함



## 어트리뷰트

---

* 엔티티의 구성 요소
* 엔티티 또는 관계가 갖는 성징이나 특성
* ER 다이어그램에서는 타원으로 표현
* 엔티티는 반드시 하나 이상의 키 어트리뷰트를 가지고 있어 나머지 어트리뷰트를 유일하게 정의할 수 있음
* 예시로 학생 한 명이 가지고 있는 학번, 성적, 수강 과목, 이름 등이 어트리뷰트(Attribute)이다
* 종류
  * **단순 어트리뷰트**
  * **키 어트리뷰트(key Attribute)**
    * 엔티티들을 식별할 수 있는 유일한 제약조건을 갖는다
  * **복합 어트리뷰트(Multi Attribute)**
    * 두 개 이상의 어트리뷰트로 이루어져 있음
    * 각각의 어트리뷰트는 그 자체로도 독립적인 의미를 가짐
  * **다치 어트리뷰트(Multivalue Attribute)**
    * 어트리뷰트 하나에 여러 값이 들어갈 수 있는 어트리뷰트
  * **유도된 어트리뷰트(Derived Attribute)**
    * 실제 값이 저장되어 있는 것이 아닌 저장된 값으로부터 계산해서 얻은 값을 사용하는 어트리뷰트
  * **부분 키(Partial Key)**
    * 키와 비슷하지만 완벽하게 키라고 할 수 없고 약한 엔티티에서만 사용되는데, 키 어트리뷰트에 반해서 부분키라고 함
    * ER 다이어그램에서 점선으로 밑줄로 표현



## 관계

---

* 엔티티 간 관계를 나타내는 것으로, 1:N, 1:1, M:N으로 표현할 수 있음 -> 카디널리티 비율(Cardinality Ratio)
* 엔티티 간 존재하는 수학적 관계를 말함
* 관계는 관계형 데이터베이스로 매핑
* ER 다이어그램에서는 마름모로 표현



## 엔티티 타입

---

* 여러 엔티티가 모여서 하나의 집단을 이룬 형태
* ER 다이어그램에서 엔티티 타입은 사각형으로 표현
* 두가지 종류가 있는데 강한 엔티티타입과 약한 엔티티 타입이 있음
  * 강한 엔티티 타입
  * 약한 엔티티 타입: 자신의 키 어트리뷰트가 없는 엔티티 타입을 말함