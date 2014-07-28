// #pragma once
#ifndef SOLUTION
#define SOLUTION

#include"string"
#include"iostream"
#include<assert.h>

using namespace std;

class solution
{

        public: 
                void strRev(string &s);

//protected:

};

void solution::strRev(string &s)
{

        int wordLen = 0, len, start = s.length();

        string temp;

        if (s.length() != 0)
        {
                cout<<"s.length: "<<s.length()<<endl;

                while (s.length()> 0 && s.at(0) == ' ') s.erase(0, 1); // Delete the spaces ahead.

                if (s.length() == 0 ) {
                        cout<<"\nThere is no words in this sentencs. \n"<<endl;
                        return;
                }

                while (s.length() > 0 &&s.at(len - 1) == ' ') // Delete the space consecutivly.
                {
                        s.erase(len - 1, 1);

                        len = s.length();
                }


                for (int i = len - 1; i >= 0; i--)
                {
                        wordLen += 1;

                        if (i <= len - 1)
                        {
                                if (s.length() > i &&s.at(i) == ' ' && s.length() > i+1 && s.at(i + 1) != ' ')
                                {
                                        start = i;

                                        temp.append(s, start + 1, wordLen - 1);
                                        temp.append(" ");

                                        wordLen = 0;
                                }
                                else if ( s.length() > i && s.at(i) == ' ' && s.at(i + 1) == ' ')
                                {
                                        s.erase(i, 1);

                                        len = s.length();

                                        wordLen = 0;
                                }
                                else if (i == 0)
                                {
                                        start = i;

                                        temp.append(s, start, wordLen);

                                        wordLen = 0;
                                }
                        }
                }

                s.assign(temp);
        }
        else
        {
                cout<<"\nThere is no words in this sentencs. \n"<<endl;
        }
}
#endif