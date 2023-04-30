import modul_group as m_g
import modul_student as m_s

my_student = m_s.Student('male', 22, 'Ukraine', 'Ivanov')
my_sec_student = m_s.Student('female', 21, 'US', 'J')
my_th_student = m_s.Student('male', 23, 'Ukraine', 'Jecson')
my_four_student = m_s.Student('female', 20, 'US', 'TH')
my_five_student = m_s.Student('male', 26, 'US', 'KB')
my_six_student = m_s.Student('female', 21, 'US', 'M')
my_seven_student = m_s.Student('male', 19, 'US', 'CR')
my_eight_student = m_s.Student('female', 22, 'US', 'TB')
my_nine_student = m_s.Student('female', 24, 'US', 'AH')
my_ten_student = m_s.Student('male', 20, 'US', 'WB')
my_eleven_student = m_s.Student('male', 23, 'US', 'BHU')


my_group = m_g.Group()
my_group.add(my_student)
my_group.add(my_sec_student)
my_group.add(my_th_student)
my_group.add(my_four_student)
my_group.add(my_five_student)
my_group.add(my_six_student)
my_group.add(my_seven_student)
my_group.add(my_eight_student)
my_group.add(my_nine_student)
my_group.add(my_ten_student)
my_group.add(my_eleven_student)

print(my_group.search('Jecson'))
print(my_group)
