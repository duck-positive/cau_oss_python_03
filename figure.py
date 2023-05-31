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
    class line : 길이에 대한 변수 __width와  __height를 가지고 있으며, 
    외부에서는 접근이 불가능 하며 setter와 getter로 값에 접근 가능. 기본값은 0
    """
    __width = 0
    __height = 0
    def __init__(self, width, height):
        """생성자, 가로 길이를 나타내는 width와 세로 길이를 나타내는 height를 입력받을 수 있다.
        Args:
            width (int or float) : 초기 선의 가로 길이
            height (int or float) : 초기 선의 세로 길이    
        """
        self.__width = width
        self.__height = height

    def set_length(self, width, height) :
        """setter, 선의 길이를 수정할 수 있다
        Args:
            width (int or float) : 수정할 선의 가로 길이
            height (int or float) : 수정할 선의 세로 길이 
        """
        self.__width = width
        self.__height = height

    def get_length(self) :
        """getter, 객체가 저장하고 있는 선의 길이를 반환받는다.
        Returns:
            (int or float) : 선의 가로 길이
            (int or float) : 선의 세로 길이 
        """
        return self.__width, self.__height

def area_rectangle(width, height) :
    """길이를 입력받아 직사각형의 넓이를 반환하는 함수
        Args:
            width (int or float) : 직사각형의 가로 길이
            height (int or float) : 직사각형의 세로 길이 
        Returns:
            width*height (int or float) : 입력받은 가로와 세로의 곱
    """
    return width*height

def area_ellipse(width, height) :
    """길이를 입력받아 타원의 넓이를 반환하는 함수
        Args:
            width (int or float) : 짧은 쪽의 반지름 길이
            height (int or float) : 긴 쪽의 반지름 길이 
        Returns:
            width*height*π (int or float) : 타원의 넓이
    """
    return width*height*math.pi
def area_right_triangle(width, height) :
    """길이를 입력받아 직각삼각형의 넓이를 반환한다
        Args:
            width (int or float) : 밑변의 길이
            height (int or float) : 높이의 길이 
        Returns:
            width*height/2 (int or float) : 직각삼각형의 넓이
    """
    return width*height/2