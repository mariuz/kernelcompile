Compiling latest vanilla kernel with a python script

it can be used with the stable version or the release candidate one or longterm

http://mapopa.blogspot.com/2009/01/compiling-2.html

And here is howto use it on ubuntu/debian for building a RC version and then install it 

http://mapopa.blogspot.com/2009/01/building-kernel-2.html

Install Requirements 
    apt-get install python-pip
    pip install sh feedparser

Usually the script will do all the work for you , here is the example for mainline
 
    sudo python kernel-compile.py --type mainline


or for stable default


    sudo python kernel-compile.py


also a version can be provided 


    sudo python kernel-compile.py --type mainline --version 4.2
    
    

Default build type is debian way but it can be changed to normal (aka make , make install)

     sudo python kernel-compile.py -b=normal

License is GPL3 as usual
http://www.gnu.org/licenses/gpl-3.0.html
