#include <bits/stdc++.h>

// priority dequeue 를 이용
// 값과 함께 idx를 넣어서 유효함을 확인
// 유효하지 않은 값은 pop

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, L;
    cin >> N >> L;
    vector<int> arr(N);
    priority_queue<pair<int, int>> pq;

    for(int i=0;i<N;i++) cin >> arr[i];

    for(int i=0;i<N;i++) {
        pq.push({-arr[i], i});
        while(!pq.empty() && pq.top().second <= i - L) pq.pop();
        cout << -pq.top().first << " ";
    }

    return 0;
}