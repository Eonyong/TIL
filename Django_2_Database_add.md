# ORM:file_cabinet:

> 객체 지향 프로그래밍(OOP) 사용할 때 호환되지 않는 유형의 시스템 간에 데이터를 __변환__하는 프로그래밍 기술
>
> OOP 프로그래밍에서 RDBMS 연동 시, DB와 OOP간 호한되지 않는 데이터를 변환해주는 친구
>
> Django에 내장되어있음 (sqlite3인걸로 알고 있음...)
>
> DB를 객체로 조작하기 위해 사용
>
> __장점__
>
> * SQL을 잘 몰라도 DB조작 가능
> * SQL의 절차적 접근이 아닌 OOP 접근으로 생산성이 높음
>
> __단점__
>
> * ORM만으로 완전한 서비스 구현이 어려움

`model.py`작성

```python
# articles/model.py

class Article(model.Model):	#class 클래스 이름(상속받을 내용)
    title = model.CharField(max_length=10)	# 한줄한줄이 Field(column)
    content = model.TextField()	# ChaarField는 char 타입, TextField는 Text 타입
```



# Migrations

> "django가 model에 생긴 변화는 DB에 반영하는 방법"
>
> Migration 실행 및 DB 스키마를 다루기 위한 명령어

```bash
$ python manage.py <명령어>
```

> :star:__makemigrations__: model을 변경한 것에 기반한 새로운 마이그레이션(=설계도)을 만들 때 사용
>
> :star:__migrate__: 마이그레이션을 DB에 반영하기 위해 사용, 설계도를 실제 DB에 반영하는 과정, 모델에서의 변경 사항들과 DB의 스키마가 동기화

```bash
$ python manage.py migrate	# 한 경우, 우리가 설정한 columns과 함께 pk(primary key)도 함께 생성
```

> :speaker: pk는 __고유한 것__이어야 함. 일반적으로  index로 표시됩니다. :star2:
>
> __sqlmigrate__: 마이그레이션에 대한 구문을 보기 위해 사용, 마이그레이션 SQL문으로 어떻게 해석되어 작동할지 확인
>
> __showmigrations__: 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용, 마이그레이션 파일들이 migrate 됐는지 안됐는지 여부를 확인 가능

:warning: class 내부의 내용이 수정되면, :star: 부분 다시 실행

:wave:__반드시 기억해야 할 migration 3단계__:wave:

> 1. model.py : model 변경사항 발생 시
> 2. $ python manage.py makmigrations: migrations  파일 생성
> 3. $ python manage.py migrate: DB반영

# Database API

* DB API (python 으로 작성할 것임)

  >DB 조작을 손쉽게 하기 위한 도구 :pencil2:
  >
  >Django가 기본적으로 ORM을 제공함에 따라 DB를 편하게 조작 가능
  >
  >database-abstract API를 자동으로 만듦 (객체들을 만들고 읽고 수정할 수 있음)
  >
  >database-access API라고도 부름 

* 구문 - <Class Name>.<Manager>.<QuerySet API>() 형식
  * __Manager__

    >django 모델에 DB query 작업이 제공되는 인터페이스
    >
    >기본적으로 모든 Django 모델 클래스에 object라는 Manager 추가

  * __QuerySet__

    > DB로부터 전달받은 객체 목록
    >
    > queryset 안의 객체는 0개 ~ 여러 개
    >
    > DB로부터 조회, 필터, 정렬등을 수행 가능
    >
    > __method는 크게 2가지로 나뉨__
    >
    > 1. 새로운 queryset을 반환
    > 2. queryset을 반환하진 않음

* Django shell

  > 일반 python shell을 통해서는 Django 프로젝트 환경에 접근 불가
  >
  > 기본 Django shell보다 더 많은 기능을 제공하는 shell_plus를 이용하여 shell 진행
  >
  > ```shell
  > Data를 입력한 뒤에는
  > $ <class name>.save() 는 필수!!!
  > ```

# CRUD

* 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리기능인

  Create, Read, Update, Delete를 묶어서 일컫는 말

