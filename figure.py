import math

"""
figure 모듈 구성
- class line : 길이에 대한 private 변수 length를 가지고 있으며, 
setter와 getter로 값 변경 가능. 기본값은 0
- area_square(int) : 길이를 매개변수로 받아 정사각형의 넓이를 반환하는 함수
- area_circle(int) : 길이를 매개변수로 받아 원의 넓이를 반환하는 함수
- area_triangle(int) : 길이를 매개변수로 받아 정삼각형의 넓이를 반환하는 함수

"""
class line :
    """
    class line : 길이에 대한 변수 __length를 가지고 있으며, 
    aetter와 getter로 값 변경 가능. 기본값은 0
    """
    __length = 0
    def __init__(self, initial_value = 0):
        """생성자, __length의 길이를 입력받을 수 있다.
        Args:
            initial_value : 길이 입력값, 기본값 0
        Returns:
            
        Examples:
            >>> line = figure.line(10) # __length를 10으로 해서 인스턴스화한다
        """
        self.__length = initial_value

    def set_length(self, length) :
        """setter, __length의 길이를 설정할 수 있다.
        Args:
            length : 설정할 길이
        Returns:
            
        Examples:
            >>> line.set_length(10) # line의 __length를 10으로 설정한다
        """
        self.__length = length

    def get_length(self) :
        """getter, __length의 길이를 반환받는다.
        Args:
            
        Returns:
            __length : 설정된 길이
        Examples:
            >>> line.get_length() # line의 __length를 반환받는다
        """
        return self.__length

def area_square(length) :
    """길이를 입력받아 정사각형의 넓이를 반환한다
        Args:
            length : 계산할 길이
        Returns:
            length*length : 입력받은 길이를 한 변으로 하는 정사각형의 넓이
        Examples:
            >>> area_square(10) # 10*10 의 결과 100을 반환받는다
    """
    return length*length
def area_circle(length) :
    """길이를 입력받아 원의 넓이를 반환한다
        Args:
            length : 계산할 길이
        Returns:
            length*length*π : 입력받은 길이를 반지름으로 하는 원의 넓이
        Examples:
            >>> area_circle(10) # 10*10*π 의 결과 314.1...을 반환받는다
    """
    return length*length*math.pi
def area_regular_triangle(length) :
    """길이를 입력받아 정삼각형의 넓이를 반환한다
        Args:
            length : 계산할 길이
        Returns:
            (math.sqrt(3)/4)*length*length : 입력받은 길이를 한 변으로 하는 정삼각형의 넓이
        Examples:
            >>> area_circle(10) # (math.sqrt(3)/4)*10*10 의 결과 43.3...을 반환받는다
    """
    return (math.sqrt(3)/4)*length*length