음취헌 Piano Manager 🎹
=======

음취헌은 성균관대 자연과학캠퍼스 복지회관 3층에 있는 고전음악 감상실입니다. 주요 활동으로는 그랜드피아노 자유 이용, 주 2시간 내외의 운영, 매년 연주회 및 홈커밍데이 등 여러 행사가 있습니다. 교내 구성원이라면 누구든 가입할 수 있으며, 실원은 상시 모집 중입니다. 관련 문의 사항은 운영진에게 연락 바랍니다.  

이 repository는 음취헌 피아노 사용 기록용 프로그램입니다. 그랜드 피아노 이용 시 사용 기록을 데이터베이스에 기록하며, 이를 웹페이지를 통해 접근할 수 있도록 하는 것이 저희의 목표입니다. 원하는 기능이 있다면 제작진([contributors](#contributors))에게 메일 등으로 문의하거나, issue로 등록하면 됩니다.  

이 repository는 Raspberry Pi를 위해 만들어졌으며, 주된 기능은 다음과 같습니다.  
- 전화번호 혹은 NFC를 이용한 사용시간 체크
- 사용시간을 DB에 기록 (현재 aws 사용 중)

---

## ✔ Guideline
### Setting ⚙
해당 repository를 다운로드 받으세요. git을 이용해 받는 것을 권장합니다.  
git을 이용해서 받으려면, 우선 [git을 설치](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)하고 원하는 경로에서 다음 명령어를 입력하세요.  
```shell
git clone https://github.com/dotoleeoak/skku-hun-2020
```
파일을 모두 받았으면, 제작진([@dotoleeoak](https://github.com/dotoleeoak))에게 db.py를 받아 model 폴더에 넣어주세요.  
(해당 파일은 보안의 문제로 GitHub에 업로드하지 않았습니다.)  

> ~~requirements.txt 설명 추가 필요~~  

이후 python으로 main.py를 실행하면 됩니다.  

### NFC 관련 주의 사항 ⚠
- 라즈베리파이에서 NFC를 사용할 경우:  
    ```python
    from NFC.NFCReader import NFCReader
    ```
    
- 이외의 경우(windows에서 실행 테스트, 디버깅 등):  
    ```python
    from NFC.NFCReaderForTest import NFCReader
    ```

---

## 😎 Contributors
- 김정원 [@threedalpeng](https://github.com/threedalpeng) - UI 구현 (고생 많았다 ㅎㅎ)  
- 김주현 [@juhy0987](https://github.com/juhy0987) - DB 구성  
- 이진영 [@HopangLee](https://github.com/HopangLee) - UI 디자인  
- 최재민 [@dotoleeoak](https://github.com/dotoleeoak) - UI, DB 연결  

---

> ~~내용 추가 예정~~
