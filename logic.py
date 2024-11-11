class square:
    def __init__(self, n, is_movable):
        self.num = n
        self.is_movable = is_movable

class State:
    def __init__(self, m):
        self.m = m
        self.movable_positions = [index for index, square in enumerate(m) if square.num not in (0, 1) and square.is_movable]

    def move(self, direction):
        v = 1  # متغير للتحقق من الحركة
        while v >= 0 and self.movable_positions:
            v = 0  # إعادة تعيين المتغير في بداية كل جولة
            for pos in self.movable_positions:
                moved = False
                if direction == 'right':
                    moved = self.move_right(pos)
                elif direction == 'left':
                    moved = self.move_left(pos)
                elif direction == 'down':
                    moved = self.move_down(pos)
                elif direction == 'up':
                    moved = self.move_up(pos)
                
                if moved:
                    v += 1
                else:
                    v -= 1

            # تحديث قائمة المربعات القابلة للحركة بعد كل جولة
            self.movable_positions = [index for index, square in enumerate(self.m) if square.num not in (0, 1) and square.is_movable]

        return State(self.m)

    def move_right(self, pos):
        target = pos + 1
        if self.check_move_right(pos, target):
            if self.m[target].num == 0:  # إذا كانت الخانة الهدف فارغة
                self.m[pos], self.m[target] = self.m[target], self.m[pos]  # تبادل المواقع
                return True
            elif self.m[pos].num == self.m[target].num:  # إذا كانت الأرقام متساوية
                self.m[pos].num = 0
                self.m[target].num = 0
                return True
        return False

    def move_left(self, pos):
        target = pos - 1
        if self.check_move_left(pos, target):
            if self.m[target].num == 0:  # إذا كانت الخانة الهدف فارغة
                self.m[pos], self.m[target] = self.m[target], self.m[pos]  # تبادل المواقع
                return True
            elif self.m[pos].num == self.m[target].num:  # إذا كانت الأرقام متساوية
                self.m[pos].num = 0
                self.m[target].num = 0
                return True
        return False

    def move_down(self, pos):
        target = pos + 6  # الانتقال إلى الأسفل
        if self.check_move_down(pos, target):
            if self.m[target].num == 0:  # إذا كانت الخانة الهدف فارغة
                self.m[pos], self.m[target] = self.m[target], self.m[pos]
                return True
            elif self.m[pos].num == self.m[target].num:  # إذا كانت الأرقام متساوية
                self.m[pos].num = 0
                self.m[target].num = 0
                return True
        return False

    def move_up(self, pos):
        target = pos - 6  # الانتقال إلى الأعلى
        if self.check_move_up(pos, target):
            if self.m[target].num == 0:  # إذا كانت الخانة الهدف فارغة
                self.m[pos], self.m[target] = self.m[target], self.m[pos]
                return True
            elif self.m[pos].num == self.m[target].num:  # إذا كانت الأرقام متساوية
                self.m[pos].num = 0
                self.m[target].num = 0
                return True
        return False

    def check_move_right(self, pos, target):
        return target < len(self.m) and (self.m[target].num == 0 or self.m[target].num == self.m[pos].num)

    def check_move_left(self, pos, target):
        return target >= 0 and (self.m[target].num == 0 or self.m[target].num == self.m[pos].num)

    def check_move_down(self, pos, target):
        return target < len(self.m) and (self.m[target].num == 0 or self.m[target].num == self.m[pos].num)

    def check_move_up(self, pos, target):
        return target >= 0 and (self.m[target].num == 0 or self.m[target].num == self.m[pos].num)

    def print_board(self):
        for i in range(0, len(self.m), 6): 
            print(" ".join(str(square.num) for square in self.m[i:i+6]))
        print()
    def check_win_condition(self):
        # التحقق من أن الرقعة تحتوي فقط على الأرقام 0 و 1
        return all(square.num in (0, 1) for square in self.m)
    
    def next_state(self):
          v = 1  # متغير للتحقق من الحركة
          while v >= 0 and self.movable_positions:
            v = 0  # إعادة تعيين المتغير في بداية كل جولة
            for pos in self.movable_positions:
                moved = False
                moved = self.move_right(pos)
              
                
                if moved:
                    v += 1
                else:
                    v -= 1
            self.movable_positions = [index for index, square in enumerate(self.m) if square.num not in (0, 1) and square.is_movable]

          obj1= State(self.m)
          n = 1  # متغير للتحقق من الحركة
          while n >= 0 and self.movable_positions:
            n = 0  # إعادة تعيين المتغير في بداية كل جولة
            for pos in self.movable_positions:
                moved = False
                moved = self.move_left(pos)
              
                
                if moved:
                    n += 1
                else:
                    n -= 1
            self.movable_positions = [index for index, square in enumerate(self.m) if square.num not in (0, 1) and square.is_movable]
            obj2= State(self.m)
            z = 1  # متغير للتحقق من الحركة
          while z >= 0 and self.movable_positions:
            z = 0  # إعادة تعيين المتغير في بداية كل جولة
            for pos in self.movable_positions:
                moved = False
                moved = self.move_up(pos)
              
                
                if moved:
                    z += 1
                else:
                    z -= 1
            self.movable_positions = [index for index, square in enumerate(self.m) if square.num not in (0, 1) and square.is_movable]
            obj3= State(self.m)
            c = 1  # متغير للتحقق من الحركة
          while c >= 0 and self.movable_positions:
            c = 0  # إعادة تعيين المتغير في بداية كل جولة
            for pos in self.movable_positions:
                moved = False
                moved = self.move_down(pos)
              
                
                if moved:
                    c += 1
                else:
                    c -= 1
            self.movable_positions = [index for index, square in enumerate(self.m) if square.num not in (0, 1) and square.is_movable]

          obj4= State(self.m)
          return (obj1,obj2,obj3,obj4)