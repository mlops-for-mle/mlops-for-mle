# MLOps for MLE

본 저장소는 [MLOps for MLE](https://mlops-for-mle.github.io/tutorial/) 의 실습 코드가 구현되어있는 저장소입니다.
먼저 각 파트 문서를 통해 진행 방향을 확인하고 구현에 도전합니다.
코드를 바로 실행하기보다는 직접 구현하면서 실제 구현체와의 차이를 확인하는 방식으로 진행하는 것을 권장합니다.

문서에 명시된 파일 이름과 같은 파일들로 구성되어 있으며, 참고가 필요할 경우 해당 파일을 확인하면 됩니다.


## Usage
구현체가 있는 경우 디렉토리의 구성은 다음과 같습니다.
```bash
part_no
    ├── Makefile
    ├── implementation1.py
    ├── implementation2.py
    └── ...
```
먼저 파트의 디렉토리로 이동합니다.
```bash
$ cd part_no
```
이동 후 같은 디렉토리에서 `make server` 명령어를 통해 파트의 구현체를 바로 띄워볼 수 있습니다.
```bash
$ make server
```
단, 각 파트마다 선행되어야 하는 부분이 있는 경우 `make dependency` 명령어를 수행하여 선행 파트의 구현체를 띄워야 합니다.
```bash
$ make dependency
$ make server
```
두 가지 작업을 한번에 실행하려면 `make all` 명령어를 사용해주세요.
```bash
$ make all
```

실습이 종료되었다면 해당 파트의 구현체를 종료시키기 위해 기존 명령어에 `-clean` 을 붙여 프로세스를 정리합니다.

```bash
$ make server-clean
```
```bash
$ make dependency-clean
```
두 가지 작업을 한번에 종료하려면 `make all-clean` 명령어를 사용해주세요.
```bash
$ make all-clean
