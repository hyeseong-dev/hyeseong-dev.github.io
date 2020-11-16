# AWS의 RDS를 이용 -  DB 구축

## Why? RDS

 이전 시간에는 PHP컨테이너와 MySQL컨테이너로 서로 연동해보았지만 DB영속성이 없다는 문제점이 마지막에 언급했습니다.   
이번에는 이를 해결하고자 하는 방법중에 하나를 알아볼게요. 

**AWS\(Amazon Web Services\) - RDS**를 이용해서  데이터의 영속성을 유지해 볼게요.   
즉, 한번 기록된 데이터를 컨테이너가 꺼지더라도 데이터가 남아있도록 하기위해서 AWS - RDS를 이용하는거에요.   
 

### How? 

####  AWS - RDS 웹페이지로 가주세요.

* 데이터베이스 생성 버튼을 눌러주세요. 

> 이대로 DB생성을 하게 되면 UTF-8 설정이 적용되지 않아 한글 출력에 문제가 발생해요.

###  파라미터 설정 

* 다시 뒤로가기를 눌러 RDS 메인 페이지로 가주세요.
* 왼쪽 사이드바의 '파라미터 그룹'을 클릭하세요
* '파라미터 그룹 생성' 버튼을 눌러 주세요. 

  * '파라미터 그룹 패밀리'란에 - **mysql5.6 입력**
  * **'그룹이름'과 '설명' -** docker-mysql-test를 각각 입

* 생성 버튼 클릭 
* 생성이 되었으면 docker-mysql-test 클릭후 '파라미터그룹작업' 박스를 클릭해서 '편집'을 클릭하세요. 
* '파라미터 필터링'이라고 희미하게 쓰여진 검색창에 'char'을 입력하세요. 
* 여러 목록들중 utf-8이 선택 가능한것들을 모두 utf-8로 바꿔주세요.

  *  character\_set\_client
  *  character\_set\_connection
  * character\_set\_filesystem
  * character\_set\_results
  * character\_set\_server

* '변경 사항 저장' 버튼 클
* 'collation'을 검색하여 collation\_connection과 collation\_server 두 부분에 utf8\_general\_ci를 둘다 선택하고 저장해주세요.

위 작업은 한글 데이터 삽입이 가능한 DB를 위해서 한글 설정 관련 파라미트 그룹을 만들어 준거에요. 

> 파라미터 그룹은 데이터베이스 설정에 관한 부분이에요.   
> 결국 그 설정은 한글 사용이 원할하도록 UTF-8을 해주겠다는 말이에요.



### DB 생성 

1. **AWS - RDS 웹페이지로 가서 데이터베이스 생성버튼을 클릭**
2. **MySQL 선택**
3. 버전은 Docker에 설치된 mysql5.6.40버전
4. **'프리 티어'에 check**
5. **설정에서 DB인스턴스 식별자 입력란은 docker-mysql-test로 입력**
6. **마스터 사용자 이름은 user로 입력**
7. 비밀번호는 간단한걸로 설정해주세요.\(까먹지 않게\)
8. 연결 카테고리에서 퍼블릭 액세스 가능성에 '예'를 선택 - 세계 어디에서나 내 DB를 접속할 수 있도록 설정함.
9. 데이터베이스 옵션 -&gt; 데이터베이스 이름을 TEST로 입
10. DB 파라미터 그룹 -&gt; docker-mysql-test 파라미터를 설
11. 이외의 것들은 기본 설정 상태로 두시면 되요. 
12. DB식별자에 docker-mysql-test 인스턴스가 생성됬어요. 
13. 클릭 -&gt; 보안 그룹\(VPC 보안그 -&gt; 인바운드 규칙 \(편집\)-&gt; 

* 유형 : MYSQL/Aurora
* 프로토콜 : TCP
* 포트 범위: 3306
* 소스: 사용자 지정 -  0.0.0.0/0

즉, 누구나 해당 RDS의 주소만 알고 있으면 접속 할 수 있는 상태로 만들었어요.

## PHP와 RDS 연동 인트

1. 엔드 포인트 주소를 복사해서  
2. /home/ubuntu/example/html/index.php 경로의 파일을 수정할게요. 

![](../../.gitbook/assets/image%20%28217%29.png)



```text
<?php 
    $conn = mysqli_connect(
    'docker-mysql-test.czwklgfqj2jp.us-east-2.rds.amazonaws.com', # 엔드포인트 입
    'user', # RDS 생성시 정한 사용자 이름 
    'password',
    'TEST',
    '3306'    # MySQL 기본포트 3306으로 바꿔주세요
    );
    if(mysqli_connect_errno()) {
        echo "Failed to connect to MySQL: ".mysqli_connect_error();
    }
    $sql = "SELECT VERSION()";
    $result = mysqli_query($conn, $sql);
    $row = mysqli_fetch_array($result);
    print_r($row["VERSION()"]);
?>

```

 3번째 줄은 RDS 생성후에 할당 되는 '엔드포인트'를 입력해주세요. 

4번째 줄은 RDS 생성 시에 정한 사용자 이름을 입력하시고요. 

5번째 줄은 비밀번호, 6번째 줄은 DB 이름, 7번째 줄은 포트번호\(기본 MySQL\) 

위 소스코드를 저장하고 다시 본인 EC2 아이피로 접속해주세요.   
 그럼 이전에 MySQL Version이 나오도록 쿼리문을 입력했는데.5.6.40-log 으로 출력된다면 정상적으로 나타난거에요. 

##  요약 

### 1. AWS - RDS 구축 

* 더이상 MySQL 컨테이너를 이용하지 않아 안전하게 기록하고 관리할 수 있는 DB를 만들게 된거임 
* 실제 현업에서도 AWS RDS를 이용함 

#### 추가 EC2서버의 MySQL 컨테이너를 삭제

 이제 EC2 서버안의 MySQL 컨테이너를 삭제해도 아무런 문제가 없어요.

```text
docker rm -f MySQL컨테이너ID
```



