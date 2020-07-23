#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    int answer = 0;
    while(answer <=500 && num !=1){
        if(num%2==0){
            num/=2;
        }
        else if(num%2==1){
            num=num*3+1;
        }
        answer++;
    }
    if(answer>500){
        answer = -1;
    }
    return answer;
}
