# 코드 개선을 위한 Collection 사용
> :bulb: 코드 개선을 위한 Collection 사용

## 목표
- collection에 대한 이해
- collection을 활용해서 코드 개선

## Collection에 대한 이해
- Colletion이란 Stack, Queue, Array, List, Hash, Map, Dictionary 같은 데이터를 그룹으로 저장할 수 있는 메모리 구조를 말합니다.

## Collection을 활용해서 코드 개선
- List 활용

  - ```python
    from datetime import date
    
    
    def fc_day(month):
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29
            else:
                return 28
        else:
            if month in day_30:
                return 30
            elif month in day_31:
                return 31
    
    
    year, month, day = str(date.today()).split('-')
    year, month, day = int(year), int(month), int(day)
    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]
    
    print(fc_day(month))
    
    ```

- dictionary 활용

  - ```python
    from datetime import date
    
    
    def fc_day(month):
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29
            else:
                return 28
        else:
            return day_dict.get(month)
    
    
    year, month, day = str(date.today()).split('-')
    year, month, day = int(year), int(month), int(day)
    day_dict = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    print(fc_day(month))
    ```

## 참고자료
- https://docs.python.org/ko/3/tutorial/datastructures.html
- https://docs.python.org/ko/3/tutorial/datastructures.html#dictionaries

## 과제제출
- [기본과제](기본과제)
- [심화과제](심화과제)