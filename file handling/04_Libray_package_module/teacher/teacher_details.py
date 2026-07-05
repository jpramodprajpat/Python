import os , sys;
from os.path import dirname , join , abspath;
parent_dirpath = abspath(join(dirname(__file__) , ".." ));
sys.path.insert(0, parent_dirpath)

from student import student_details;
def teacher() :
    print("This is Teacher details")

student_details.student();




