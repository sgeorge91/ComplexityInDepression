//Uniform Deviates
#include<iostream>
#include <fstream>
#include <math.h>
#include<stdlib.h>
#include<string>
#include <sstream>
/*This program reads a one column file name from the command line, reads the time series, converts it imnto a uniform deviate and writes the uniform deviate output into a file named ud_<filename>*/
using namespace std;
int main(int argc,  char* argv[])
{

string a[10000],fnp,fnpp;
ifstream fin;
double t1,t2;
ofstream fout;
string fn;
float u[10000];
int N;

if (argc<3)
{
cout<<"Usage ./UD.out <Fname> <#Points>\n";
return(0);
}
else
{
fn=argv[1];
N=stof(argv[2]);
}
fin.open(fn);
fnpp="ud_";
fnp=fnpp+=fn;
fout.open(fnp);
for(int i=0;i<N;i++)
{
fin>>a[i];
}
for(int i=0;i<N;i++)
for(int j=0;j<N;j++)
{
if (a[i]>a[j])
	u[i]=u[i]+1;
}

for(int i=0;i<N;i++)
{
u[i]=u[i]/N;
}
for(int i=0; i<N;i++)
fout<<u[i]<<'\n';

return 0;
}
