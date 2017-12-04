"""
# Print Rocketships
by wisemonkey
20171203 at 10:51 pm
v1.0.0

I wanted to write an old project in python
the projects prints me some dam simple rocketshipts in the command line
"""

import unittest


class Draw():
    '''
    draws a line
    example
    "********"
    or
    "*      *"
    '''
    length = 0
    character = ''
    space = ''

    finished_line = ''

    # def __init__(self, length, char):
    #     '''no return
    #     draw line setup ininilations
    #     '''
    #     self.length=length
    #     self.character=char

    def __init__(self, length, char, space=" "):
        '''no return
        draw line setup ininilations
         n = 0 % 2
        * n = 1
        ** n = 2
        *#* n = 3
        *##* n =4
        '''
        self.length = length
        self.character = char
        self.space = space

    def line(self, length):
        '''
        modifys the ouput private vairable
        :return:
        '''
        self.finished_line = length * self.character
        return self.finished_line

    def sides(self, center):
        """

        :rtype: basestring
        """
        self.finished_line = '{}{}{}'.format(self.character, self.space * (center - 2), self.character)
        return self.finished_line


    def pattern_from_list(self, patterns):

        for pattern in patterns:
            if pattern:
                self.finished_line += "$"
            elif pattern is False:
                self.finished_line += self.space

    def __str__(self):
        return self.finished_line

    def show(self):
        print("{}{}{}".format(">", self, "<"))


class Build():
    '''
    create stage of the rocket
    '''
    # self.height=0
    width = 0
    char = ''
    space = ''
    grid = ['']

    def __init__(self, height, width, char="*", space=" "):
        self.height = height
        self.width = width
        self.char = char
        self.space = space

    def stage(self):
        size = self.width

        top = Draw(size, self.char, self.space)
        top.line(size)

        self.grid.append(top)
        for i in range(0, self.height -2):
            row1 = Draw(size, self.char ,self.space)
            row1 = row1.sides(size)
            self.grid.append(row1)
        self.grid.append(top)

    def even_code(self):
        print("TODO P")

        print('{}{}{}'.format('1','T','TD'))
        return "TODO RET"
    def show(self):
        print(self)

    def __str__(self):
        temp = ''
        for row in self.grid:
            temp= '{}{}\n'.format(temp,row)
        return temp


# class TestDrawMethods(unittest.TestCase):
#     def test_line_empty(self):
#         test = Draw(5, "*")
#         test.line(5)
#         # print("ERROR DrawLine.__str__() your line is empty!")
#         self.assertNotEqual(str(test), '')
#         # self.assertIs(type(0)==test)
#
#     def test_line_sides(self):
#         test = Draw(5, "*","#")
#         test.sides(4)
#
#     def test_pattern_from_list(self):
#         test = Draw(5, "*")
#         test.pattern_from_list([True, False, False, False, True])
#         test.show()
#
#     def test_pattern_from_list_special_space_char(self):
#         test = Draw(5, "*", '#')
#         test.pattern_from_list([True, False, False, False, True])
#         test.show()
    pass


class TestBuildMethods(unittest.TestCase):
    # def test_init_build(self):
    #     t1 = Build(5, 5,"$","1")
    #     print("Build")
    #     t1.show()
    #     print(t1)
    # def test_stage(self):
    #     t2 = Build(5,15,"#","2")
    #     t2.stage()
    #     print("-----------------")
    #     print(t2)
    #     print("-----------------")
    #
    # def test_stage_lessthan_0(self):
    #     t3 = Build(5,5,"#","3")
    #     t3.stage()
    #
    #     print("-----------------")
    #     print(t3)
    #     print("-----------------")
    def test_cone(self):
        i = 5
        t4 = Build(i,i,"%","4")
        t4.even_code()
        print("test_cone(): ".format())
    pass


welcome_message = "Rocket Printing Program has Started!\n" \
                  + "Enter width, height, number of stages!\n" \
                  + "Width  : {}\n".format(6) \
                  + "Height : {}\n".format(4) \
                  + "Stages : {}\n".format(3)

# floor = Draw(5, "*")
print(welcome_message)

print("Testing draw_line Class")
#
# print("Call Drawline.line()")
# floor.line(4)
#
# print("Call Drawline.show()")
# floor.show()
#
# print("Call Drawline.show()")
# floor.sides(4)
# floor.show()
#
# print("Draw Drawline.__str__()")
# print(">", floor, "<")

string = ''
i = 0
# for x in range(5,-1,-1):
#     # string = '1'*x \
#     #          +'2'*i  \
#     #          +'3'*x \
#     #          + '4'*i \
#     #          + '\n'
#     string += "{}{}{}\n".format('1'*x, '2'*i, '4'*i)
#     print(string)
#
#     i -= 1

for indx in range(0,4):
    string = string +( "#" * indx)
    print(string)

second=''
# for x in range(0,5):
#     second +=
#     print(second)
#
#     i -= 1
for x in range(0,5):
    print(second[x], string[x])

# for x in range(0,5):
#     string = '1' * x
#     print(string)
#     i+=1
#     # print('{}{}{}'.format('2' * x, 'T' * f, 'TD'))
if __name__ == '__main__':
    unittest.main()
