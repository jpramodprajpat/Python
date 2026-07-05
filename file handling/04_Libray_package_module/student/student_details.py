import os ,sys
from os.path import dirname , abspath , join 
parent_dirpath = abspath(join(dirname(__file__) , ".." ));
sys.path.insert(0, parent_dirpath)
# at index -0 : add this directory to beggining of module search/ system path
# it allows to search module and packages
from teacher import teacher_details
def student() :
    print("This is Student details")

teacher_details.teacher();

#__file__ >> Gives you path containing your current script
# dirname() >> Gives you directory containing your current script
# join >> Join two or more path , inserting '/' as needed
# abspath() >> convert the relative path to absolute path

#__pyacache__ >> also called pyc file >> compiled python file >>sc to btye code>> stored in .pyc file inside __pycache__ directory
# this speed up loading 