#include"iostream"
#include"string"
#include"solutions.h"

using namespace std;

int main(void)
{
        string myStr("             ");

        solution mySln; 

        cout << myStr << endl;
        
        mySln.strRev(myStr);

        cout << myStr << endl;

        if(myStr.length() > 0){
        	 cout << myStr.at(0) << endl;
        }
       
}
