#include <iostream>
using namespace std;

int main() {
    //data type variable name = value;
    long age;
    cout << "Enter your Age: ";
    cin >> age;

    long ageSeconds = age * 365 * 24 * 60 * 60;

    cout << "Your age in seconds is: " << ageSeconds << endl;
}