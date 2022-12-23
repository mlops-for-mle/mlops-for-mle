# Chapter 6. Model Deployment

이 챕터를 실행하기 위해서는 Chapter 1의 database와 Chapter 3의 model registry가 필요합니다.
만약 실행하지 않았다면 아래 명령어를 통해 실행합니다.

```bash
$ make dependency
```

실습이 종료된 후 관련된 dependency를 다음과 같이 제거할 수 있습니다.
```bash
$ make dependency-clean
```

실행 후 [http://localhost:5001/](http://localhost:5001/) 에 접속해 run id 를 확인합니다.

확인한 run id를 이용해 아래 스크립트를 실행합니다.

```bash
$ python download_model --run-id `<RUN-ID>`
```
