#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <direct.h>
#include <fstream> 
#include <filesystem>
#include <unistd.h>
#include <sstream>

using namespace std;

int main(int argc, char* argv[])
{
  if(strcmp(argv[1],"new")==0){
    cout << "Creating new project. Note that the file will be created in the folder you are in.";
    std::ofstream outfile ("main.ph");
    outfile << "send('Hello World!')" << std::endl;
    outfile.close();
    system("code .");
} else if (strcmp(argv[1],"-l")==0){
      system((std::string("python \"C:/Phoneguytech/PH_Code/load.py\" -l") + argv[2]).c_str());
} 
}

