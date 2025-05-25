#include <iostream>
using namespace std;

int main(){
	cout<<"HelloFromC++!"<<endl;
	return 0;
}

/*
BEGIN main () "\"fib.py\" mt dd object {lang: \"Python\", version: [\"3\", \"13\"], char: \"utf-8\"}" {
	RETURN str """
code dd str \"\"\"
class Foo:
	def play(self):
		print(\\"Hello, world!\\")
\"\"\"
"""
}

BEGIN main () "\"main.py\" mt dd object {lang: \"Python\", version: [\"3\", \"13\"], char: \"utf-8\"}" {
	RETURN str """
code dd str \"\"\"
import fib
a = fib.Foo()
a.play()
\"\"\"
"""

RUN main
}
*/