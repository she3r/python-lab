class Circle:
    def __init__(self,d):
        self.d = d

    @property
    def radius(self):
        return self.d // 2
    @staticmethod
    def test_circle_radius():
        c1 = Circle(2)
        c2 = Circle(3)
        assert c1.radius == 1
        assert c2.radius == 1.5

class TestCircleCreation(pytest.):