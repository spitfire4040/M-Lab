
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
	string t1, t2, t3, t4, t5, inFileName1, inFileName2, outFileName, num, temp;
	ofstream fout;
	stringstream ss;
	int i, counter1, counter2, tracecount = 0;
	u_long num1;

	// set string values
	t1 = "april_";
	t2 = "_unique_trace";
	t3 = "_all_trace";
	t4 = "_tracecount";

	// initialize sets and iterators
	set<string> unique_trace;
	set<string>::iterator unique_trace_iterator;
	multiset<string> all_trace;
	multiset<string>::iterator all_trace_iterator;

	// iterate through all days
	for (i = 1; i < 2; i++)
	{

		// convert i to string
		num = to_string(i);

		// set file name
		inFileName1 = t1 + num + t2; // unique_trace
		inFileName2 = t1 + num + t3; // all_trace
		outFileName = t1 + num + t4; // trace_count

		// open files
		fin1.open(inFileName1);
		fin2.open(inFileName2);
		fout.open(outFileName);

		// read unique traces into set
		while (fin1.good())
		{
			getline(fin1,temp);
			unique_trace.insert(temp);
		}

		// read all traces into multiset
		while (fin2.good())
		{
			getline(fin2,temp);
			all_trace.insert(temp);
		}

		// iterate through each value in the unique map and see how many are in the multimap
		for (unique_trace_iterator = unique_trace.begin(); unique_trace_iterator != unique_trace.end(); unique_trace_iterator++)
		{
			temp = *unique_trace_iterator;
			num1 = all_trace.count(temp);
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