
// header files
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <sstream>

using namespace std;

// main function
int main()
{
	// initialize variables
	ifstream fin1, fin2;
	string ip1, ip2, ip3, ip4, inFileName1, inFileName2, outFileName, num, temp;
	ofstream fout;
	stringstream ss;
	int i, j, counter1, counter2, tracecount = 0;
	u_long num1, num2;

	// set string values
	ip1 = "april_";
	ip2 = "_all_ip";
	ip3 = "_unique_ip";
	ip4 = "_ipcount";

	// initialize sets and iterators
	set<string> unique_ip;
	set<string>::iterator unique_ip_iterator;
	multiset<string> all_ip;
	multiset<string>::iterator all_ip_iterator;

	// iterate through all days
	for (i = 1; i < 2; i++)
	{
		// convert i to string
		num = to_string(i);

		// set file name
		inFileName1 = ip1 + num + ip2;
		inFileName2 = ip1 + num + ip3;
		outFileName = ip1 + num + ip4;

		// open files
		fin1.open(inFileName1);
		fin2.open(inFileName2);
		fout.open(outFileName);

		// read unique ips into set
		while (fin1.good())
		{
			fin1 >> temp;
			all_ip.insert(temp);
		}

		// read all ips into multiset
		while (fin2.good())
		{
			fin2 >> temp;
			unique_ip.insert(temp);
		}

		// iterate through each value in the unique map and see how many are in the multimap
		for (unique_ip_iterator = unique_ip.begin(); unique_ip_iterator != unique_ip.end(); unique_ip_iterator++)
		{
			temp = *unique_ip_iterator;
			num1 = all_ip.count(temp);
			fout << num1 << ' ' << temp << endl;
		}

		// close files
		fin1.close();
		fin2.close();
		fout.close();
	}

	// end program
	return 0;
}