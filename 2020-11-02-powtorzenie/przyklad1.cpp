#include <iostream>

int main(){

    int i;

    std::cout << "[";
    for ( i = 1; i <= 10; i++ ){
        std::cout << i * i + i << ",";
    }
    std::cout << "]" << std::endl;

}
