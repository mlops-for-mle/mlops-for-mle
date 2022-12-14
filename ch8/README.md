# Chapter 8. Stream Serving

이 챕터를 실행하기 위해서는 Chapter 6 으로 띄운 API Serving 과 Chapter 7 에서 구축한 Kafka cluster 가 필요합니다.

Chapter 6 의 API Serving 은 run-id로 인해 dependency 로 실행할 수 없습니다. `ch6` 폴더에 가서 실행하고 해당 챕터를 실행해 주세요

Chapter 7 을 실행하지 않았다면 아래 명령어를 통해 실행합니다.

```bash
$ make dependency
```

실습이 종료된 후 관련된 dependency를 다음과 같이 제거할 수 있습니다.
```bash
$ make dependency-clean
```
